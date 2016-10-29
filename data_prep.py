#! /usr/bin/env python

import os
import os.path
import sys
import subprocess

zeroes = []
ones = []
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man/' + str(fn))
    #if fn.startswith('0'):
    zeroes.append(f) 
print zeroes
          # => training set
   # elif fn.startswith('1'):
        #ones.append(fn)     # => test set
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man'):
    for f in fn:
        ones.append(f) 

def text(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        transcript = basename[:-1]
        results.append("{} {}".format(basename.split('.')[0], transcript))

    return '\n'.join(sorted(results))

with open('data/train_digits/text', 'w') as train_text, open('data/test_digits/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results= []
    for filename in filenames:
        basename = filename.split('.')[0]
        results.append("{} {}".format(basename.split('.')[0], '/home/u/fall15/atruber/tidigits/data/adults/train/man/'+filename))
    return '\n'.join(sorted(results))

with open('data/train_digits/wav.scp', 'w') as train_text, open('data/test_digits/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results =[]
    for filename in filenames:
        basename = filename.split('.')[0]
        results.append("{} {}".format(basename.split('.')[0], 'global'))
    return '\n'.join(sorted(results))

with open('data/train_digits/utt2spk', 'w') as train_text, open('data/test_digits/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generate by using Kaldi util, once you have utt2spk file.
def spk2utt(filenames):
    pass