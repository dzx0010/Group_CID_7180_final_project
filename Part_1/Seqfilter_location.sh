#!/bin/bash

#First echo the csv contents
#then split into location files based on awk conditional
#if $6= china then print $1 to China_accessions
#else if $6 = USA then print $1 to USA_accessions, etc
#later we will use head to get top 10 of each set
#and hope that works

# awk -F "," '{print $6}' COVID_Seqs.csv 
#
#for Line in COVID_Seqs.csv 
#do
awk -F "," '{if ($6 == "China*") {print $1}}' COVID_Seqs.csv >> China_accessions.txt
echo "China cases sorted"
exit 1

awk -F "," '{if ($6 == "USA*") {print $1}}' COVID_Seqs.csv >> USA_accessions.txt
echo "USA cases sorted"
exit 2

awk -F "," '{if ($6 ! "China*") && ($6 ! "USA*") {print $1}}' COVID_Seqs.csv >> Other_accessions.txt
 
#done
exit 0


