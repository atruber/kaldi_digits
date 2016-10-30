#!/bin/bash
#script for kaldi yesno tutorial
#intended to be run within kaldi_digits directory

mkdir -p data/train_digits
mkdir -p data/test_digits
./data_prep.py
utils/utt2spk_to_spk2utt.pl data/train_digits/utt2spk > data/train_digits/spk2utt
utils/utt2spk_to_spk2utt.pl data/test_digits/utt2spk > data/test_digits/spk2utt
utils/fix_data_dir.sh data/train_digits/
utils/fix_data_dir.sh data/test_digits/
mkdir dict