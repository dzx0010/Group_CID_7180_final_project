#!/bin/bash

#AccList=`awk -F ";" '{print $2}' DL_Other_sorted.txt`

#IFS=$'\n'

#for next in $AccList
#do
echo "Enter the name of a DL_ file to collect fasta sequence data: "

read var2

Acc=`cat $var2`

ShortName=`echo $var2 | awk -F "_" '{print $2}'`

#esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > Other_seqs.fasta
#done

efetch -db nucleotide -format fasta -id $Acc > "$ShortName"_seqs.fasta

echo "$ShortName seqs downloaded"



