#!/bin/bash

#Idea: Input phylo tree first
#define SHORT= awk -F {print $1}
# reference $SHORT_sorted as reference file, run through tr chain below before proceeding
#no extra colons in a .ph!

echo "Please input a _sorted.txt file for reference. "
read SORTED


cat $SORTED | tr -d " " | tr : _ > tmp_$SORTED

tmpSORT=tmp_$SORTED

echo "Please input a phylogenetic tree for labeling"
read PTREE

#attempt to grep each accession number in SORTED to find it in PTREE
#replace with corresponding location using sed

for line in $tmpSORT
do
awk -F ";" 
