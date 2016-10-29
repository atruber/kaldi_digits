#! /usr/bin/env python

import os
import os.path
import sys
import subprocess

zeroes = []
ones = []
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man/%s' % fn):
        zeroes.append('train/man/{}/{}'.format(fn,f))
          # => training set
   # elif fn.startswith('1'):
        #ones.append(fn)     # => test set
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man/%s' % fn):
        ones.append('test/man/{}/{}'.format(fn,f))   #set/gender/<spk id>/<transcription><letter>.wav

def get_spk_id(filename):
    return filename.split('/')[2]

def get_utt_id(filename): #always preceeded by spkid for sorting
    return get_spk_id(filename)+filename.split('/')[3]).split('.')[0] #<transcription><letter>

def text(filenames):
    results = []
    for filename in filenames:
        basename = get_spk_id(filename) + '_' + get_utt_id(filename)  #<spkid>_<transcription><letter>
        transcript = get_utt_id[:-1]
        results.append("{} {}".format(basename, " ".join(transcript)))
    return '\n'.join(sorted(results))

with open('data/train_digits/text', 'w') as train_text, open('data/test_digits/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results= []
    for filename in filenames:
        spkid = get_spk_id(filename)
        basename = get_spk_id(filename) + '_' + get_utt_id(filename)  #<spkid>_<transcription><letter>
        pipe = 'sph2pipe -f wav ' + '/home/u/fall15/atruber/tidigits/data/adults/' +filename + ' |'
        results.append("{} {}".format(basename, pipe)
    return '\n'.join(sorted(results))

with open('data/train_digits/wav.scp', 'w') as train_text, open('data/test_digits/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results =[]
    for filename in filenames:
        results.append("{} {}".format(get_utt_id(filename), get_spk_id(filename))
    return '\n'.join(sorted(results))

with open('data/train_digits/utt2spk', 'w') as train_text, open('data/test_digits/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generate by using Kaldi util, once you have utt2spk file.
def spk2utt(filenames):
    pass