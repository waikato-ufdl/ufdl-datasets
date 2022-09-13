#!/bin/bash

festvox_dir="./festvox"
mkdir -p $festvox_dir
coqui_dir="./coqui-stt"
mkdir -p $coqui_dir

# annotations
echo "Annotations to festvox..."
cat ./text.xml | grep fileid | sed s/\"/\'/g | sed s/"<\/fileid>"/"\" \)"/g | sed s/".*='"/"( "/g | sed s/"'>"/" \""/g > $festvox_dir/annotations.txt

# 16k Hz festvox
echo "16k Hz festvox..."
wai-annotations convert \
  from-audio-files-sp \
    -i "./48000_orig/*.wav" \
  convert-to-mono \
  resample-audio \
    -s 16000 \
  to-audio-files-sp \
    -o $festvox_dir

# coqui stt
echo "Converting to Coqui STT..."
wai-annotations convert \
  from-festvox-sp \
    -i "$festvox_dir/annotations.txt" \
  clean-transcript \
    --quotes \
  to-coqui-stt-sp \
    -o "$coqui_dir/samples.csv"

