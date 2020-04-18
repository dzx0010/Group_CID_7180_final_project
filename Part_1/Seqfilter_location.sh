#!/bin/bash

#First echo the csv contents
#then split into location files based on awk conditional
#if $6= china then print $1 to China_accessions
#else if $6 = USA then print $1 to USA_accessions, etc
#later we will use head to get top 10 of each set
#and hope that works

# awk -F "," '{print $6}' COVID_Seqs.csv 
# awk -F "," '{print $1"_"$6}' COVID_Seqs.csv >> Testawk2.txt

#for LINE in COVID_Seqs.csv 
#do
echo COVID_Seqs.csv | awk -F, '{if ($6 == "China") {print $1 >> China_accessions}}'
#echo "China cases sorted"

#awk -F, '{if ($6 == "USA*") {print $1}}' >>USA_accessions.txt
#echo "USA cases sorted"

#awk -F, '{if ($6 != "China*") && ($6 != "USA*") {print $1}}' >>Other_accessions.txt

#done



