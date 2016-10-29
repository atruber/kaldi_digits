#! /usr/bin/env python

import os
import os.path
import sys
import subprocess

zeroes = []
ones = []
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/train/man/%s' % fn):
        zeroes.append('train/man-{}_{}'.format(fn,f))
          # => training set
   # elif fn.startswith('1'):
        #ones.append(fn)     # => test set
for fn in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man'):
    for f in os.listdir('/home/u/fall15/atruber/tidigits/data/adults/test/man/%s' % fn):
        ones.append('test/man-{}_{}'.format(fn,f))

def text(filenames):
    results = []
    for filename in filenames:
        basename = filename.split('.')[0]
        transcript = basename.split('_')[1][:-1]
        results.append("{} {}".format(basename.split('.')[0], " ".join(transcript)))
    return '\n'.join(sorted(results))

with open('data/train_digits/text', 'w') as train_text, open('data/test_digits/text', 'w') as test_text:
    train_text.write(text(zeroes))
    test_text.write(text(ones))

# finish this method
def wav_scp(filenames):
    results= []
    for filename in filenames:
        basename = filename.split('.')[0]
        audio = basename sph2pipe -f wav ../tidigits/data/adults/filename.split('-')[0]/basename.split('-')[0]/basename.split('-')[1] |
        results.append("{} {}".format(basename.split('.')[0], audio)
    return '\n'.join(sorted(results))

with open('data/train_digits/wav.scp', 'w') as train_text, open('data/test_digits/wav.scp', 'w') as test_text:
    train_text.write(wav_scp(zeroes))
    test_text.write(wav_scp(ones))


# finish this method
def utt2spk(filenames):
    results =[]
    for filename in filenames:
        basename = filename.split('.')[0]
        results.append("{} {}".format(basename.split('.')[0], "{} {}".format(basename.split('.')[0])))
            return '\n'.join(sorted(results))

with open('data/train_digits/utt2spk', 'w') as train_text, open('data/test_digits/utt2spk', 'w') as test_text:
    train_text.write(utt2spk(zeroes))
    test_text.write(utt2spk(ones))


# finish this method
# note that, spk2utt can be generate by using Kaldi util, once you have utt2spk file.
def spk2utt(filenames):
    pass