#! /usr/bin/env python

import os
import os.path
import sys
import subprocess
import re

zeroes = []
ones = []
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man/%s' % fn):
        zeroes.append('adults/train/man/{}/{}'.format(fn,f))
          # => training set
   # elif fn.startswith('1'):
        #ones.append(fn)     # => test set
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man/%s' % fn):
        ones.append('adults/test/man/{}/{}'.format(fn,f))   #set/gender/<spk id>/<transcription><letter>.wav

def get_spk_id(filename):
    return filename.split('/')[0][0] + filename.split('/')[2][0] +  filename.split('/')[3]

def get_utt_id(filename): #always preceeded by spkid for sorting
    return get_spk_id(filename)+ '_' + (filename.split('/')[4].split('.')[0]) #<1st letter of set><1stletter of gender><spkid>_<transcription><letter>

def convert_digits(s):
    return s.replace('o','OH').replace('0','ZERO').replace('1','ONE').replace('2','TWO').replace('3','THREE') \
            .replace('4','FOUR').replace('5','FIVE').replace('6','SIX').replace('7','SEVEN').replace('8','EIGHT') \
            .replace('9','NINE')

def text(filenames):
    results = []
    for filename in filenames:
        basename = get_utt_id(filename)  
        transcript = convert_digits(get_utt_id(filename).split('_')[1][:-1])
        results.append("{} {}".format(basename, " ".join(transcript)))
    return '\n'.join(sorted(results))

with open('data/train_digits/text', 'w') as train_text, open('data/test_digits/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results= []
    for filename in filenames:
        basename =  get_utt_id(filename)  #<spkid>_<transcription><letter>
        pipe = 'sph2pipe -f wav ' + '/home/u/fall15/atruber/tidigits/data' +filename + ' |'
        results.append("{} {}".format(basename, pipe))
    return '\n'.join(sorted(results))

with open('data/train_digits/wav.scp', 'w') as train_text, open('data/test_digits/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results =[]
    for filename in filenames:
        uttid = get_utt_id(filename)
        spkid = get_spk_id(filename)
        results.append("{} {}".format(uttid, spkid))
    return '\n'.join(sorted(results))

with open('data/train_digits/utt2spk', 'w') as train_text, open('data/test_digits/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generate by using Kaldi util, once you have utt2spk file.
def spk2utt(filenames):
    pass