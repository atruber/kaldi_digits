#! /bin/bash

mkdir -p data/train_digits
mkdir -p data/test_digits
./data_prep_tidigits.py
#/home/u/fall15/atruber/tidigits/data/
#/home/u/fall15/atruber/tidigits/data/adults/train/man,/home/u/fall15/atruber/tidigits/data/adults/train/woman
# 

./data_prep_free.py
#/home/u/fall15/atruber/free-spoken-digit-dataset/recordings/

utils/utt2spk_to_spk2utt.pl data/train_digits/utt2spk > data/train_digits/spk2utt
utils/utt2spk_to_spk2utt.pl data/test_digits/utt2spk > data/test_digits/spk2utt
utils/fix_data_dir.sh data/train_digits/
utils/fix_data_dir.sh data/test_digits/
mkdir dict
echo -e "OW\nZ\nIY\nR\nW\nAH\nN\nT\nUW\nTH\nF\nAO\nAY\nV\nS\nIH\nK\nEH\nEY   " > dict/phones.txt  
echo -e "OH OW\nZERO Z IY R OW\nONE W AH N\nTWO T UW\nTHREE TH R IY\nFOUR F AO R\nFIVE F AY V\nSIX S IH K S\nSEVEN S EH V AH N\nEIGHT EY T\nNINE N AY N" > dict/lexicon.txt 
echo "SIL" > dict/silence_phones.txt
echo "SIL" > dict/optional_silence.txt
mv dict/phones.txt dict/nonsilence_phones.txt
cp dict/lexicon.txt dict/lexicon_words.txt
echo "<SIL> SIL" >> dict/lexicon.txt 
utils/prepare_lang.sh --position-dependent-phones false dict "<SIL>" dict/tmp data/lang
../kaldi/tools/openfst/bin/fstcompile --isymbols=data/lang/words.txt --osymbols=data/lang/words.txt --keep_isymbols=false G.txt > data/lang/G.fst
steps/make_mfcc.sh --nj 112 data/train_digits exp/make_mfcc/train_digits
steps/compute_cmvn_stats.sh data/train_digits exp/make_mfcc/train_digits
steps/train_mono.sh --nj 112 --cmd utils/run.pl data/train_digits data/lang exp/mono 
../kaldi/src/fstbin/fstcopy 'ark:gunzip -c ../kaldi_digits/exp/mono/fsts.1.gz|' ark,t:- | head -n 20
steps/make_mfcc.sh --mfcc-config conf/mfcc2.conf --nj 1 data/test_digits exp/make_mfcc/test_digits
steps/compute_cmvn_stats.sh data/test_digits exp/make_mfcc/test_digits
utils/mkgraph.sh --mono data/lang exp/mono exp/mono/graph_tgpr
steps/decode.sh --nj 1 exp/mono/graph_tgpr data/test_digits exp/mono/decode_test_digits2
steps/get_ctm.sh data/test_digits exp/mono/graph_tgpr exp/mono/decode_test_digits2