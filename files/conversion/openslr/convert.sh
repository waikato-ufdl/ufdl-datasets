#!/bin/bash

# festvox
festvox_dir="./festvox"
festvox_ann="$festvox_dir/annotations.txt"
mkdir -p $festvox_dir
rm -f $festvox_dir/*.wav
rm -f $festvox_dir/*.txt

for i in jv_id_female jv_id_male
do
  echo
  echo $i
  echo

  # annotations
  if [ "$i" = "jv_id_female" ]
  then
    cat ./$i/line_index.tsv | sed s/"\t"/" \""/g | sed s/$/"\" )"/g | sed s/^/"( "/g >> $festvox_ann
  else
    cat ./$i/line_index.tsv | cut -f1,3 | sed s/"\t"/" \""/g | sed s/$/"\" )"/g | sed s/^/"( "/g >> $festvox_ann
  fi

  # wav files
  cp ./$i/wavs/*.wav $festvox_dir
done

# coqui
echo
echo "festvox -> coqui"
echo
coqui_dir="./coqui"
coqui_ann="$coqui_dir/samples.csv"

wai-annotations convert \
  from-festvox-sp \
    -i $festvox_ann \
  clean-transcript \
    --quotes \
  discard-negatives \
  convert-to-wav \
  convert-to-mono \
  resample-audio \
    -s 16000 \
    -t kaiser_fast \
  to-coqui-stt-sp \
    -o $coqui_ann

