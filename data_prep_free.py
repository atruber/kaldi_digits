#! /usr/bin/env python

import os
import os.path
import sys
import subprocess

ones = [] #test

#/home/u/fall15/atruber/free-spoken-digit-dataset/recordings/

path = raw_input('Path to tidigits/data. For example: /home/u/fall15/atruber/free-spoken-digit-dataset/recordings: ')

def make_sets(path): 
	for f in os.listdir(path):
	    ones.append(f)

make_sets(path)

def get_spk_id(filename):
	return 'a' + 'm' + 'ja'

def get_utt_id(filename): #always preceeded by spkid for sorting
    return get_spk_id(filename)+ '_' + filename 

def convert_digits(s):
    return s.replace('o','OH').replace('0','ZERO').replace('1','ONE').replace('2','TWO').replace('3','THREE') \
            .replace('4','FOUR').replace('5','FIVE').replace('6','SIX').replace('7','SEVEN').replace('8','EIGHT') \
            .replace('9','NINE')

def text(filenames):
    results = []
    for filename in filenames:
        basename = get_utt_id(filename)  
        transcript = convert_digits(filename.split('_')[0])
        results.append("{} {}".format(basename, " ".join(transcript)))
    return '\n'.join(sorted(results))

with open('data/train_digits/text', 'w') as train_text, open('data/test_digits/text', 'w') as test_text:
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results= []
    for filename in filenames:
        basename =  get_utt_id(filename)  #<spkid>_<transcription><letter>
        pipe = '../kaldi/tools/sph2pipe_v2.5/sph2pipe -f wav ' + path +filename + ' |'
        results.append("{} {}".format(basename, pipe))
    return '\n'.join(sorted(results))

with open('data/train_digits/wav.scp', 'w') as train_text, open('data/test_digits/wav.scp', 'w') as test_text:
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results =[]
    for filename in filenames:
        spkid = get_spk_id(filename)
        uttid = get_utt_id(filename)
        basename =  get_utt_id(filename) 
        results.append("{} {}".format(uttid, spkid))
    return '\n'.join(sorted(results))

with open('data/train_digits/utt2spk', 'w') as train_text, open('data/test_digits/utt2spk', 'w') as test_text:
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generate by using Kaldi util, once you have utt2spk file.
def spk2utt(filenames):
    pass