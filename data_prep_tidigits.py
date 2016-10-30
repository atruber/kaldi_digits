#! /usr/bin/env python

import os
import os.path
import sys
import subprocess

zeroes = [] #training
ones = [] #test

path = raw_input('Path to tidigits/data. For example: /home/u/fall15/atruber/tidigits/data/')
training = raw_input ('List of path(s) to training set(s). For example: \n \'home/u/fall15/atruber/tidigits/data/adults/train/man\',\'home/u/fall15/atruber/tidigits/data/adults/train/woman\'').split(',')
test = raw_input ('List of path(s) to test set(s)').split(',')

make_sets(training, test)

def make_sets(training, test): 
    for set in training:
        for fn in os.listdir(set):
            for f in os.listdir(set +'/%s' % fn):
                a = 'adults' if 'adults' in set else 'children'
                s = 'train' if 'train' in set else 'test'
                g = 'man' if 'man' in set else 'woman'
                zeroes.append(a + '/' + s + '/' + g + '/{}/{}'.format(fn,f))

    for set in test:   
        for fn in os.listdir(set):
            for f in os.listdir(set +'/%s' % fn):
                a = 'adults' if 'adults' in set else 'children'
                s = 'train' if 'train' in set else 'test'
                g = 'man' if 'man' in set else 'woman'
                ones.append(a + '/' + s + '/' + g + '/{}/{}'.format(fn,f))   #set/gender/<spk id>/<transcription><letter>.wav

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
        pipe = 'sph2pipe -f wav ' + path +filename + ' |'
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