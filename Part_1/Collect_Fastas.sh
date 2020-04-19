#!/bin/bash

AccList=`awk -F ";" '{print $2}' China_sorted.txt`

IFS=$'\n'

for next in $AccList
do

esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > China_seqs.fasta

done
echo "China seqs downloaded"
----------------------------------

AccList2=`awk -F ";" '{print $2}' Euro_sorted.txt`
AccList3=`awk -F ";" '{print $2}' Asia_sorted.txt`
AccList4=`awk -F ";" '{print $2}' Other_sorted.txt`
AccList5=`awk -F ";" '{print $2}' USAstates_randsplit_aa`

for next in $AccList2
do

esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > Euro_seqs.fasta

done
echo "Europe seqs downloaded"
----------------------------------

for next in $AccList3
do

esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > Asia_seqs.fasta

done

echo "Asia seqs downloaded"
-----------------------------

for next in $AccList4
do

esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > Other_country_seqs.fasta

done
echo "Other country seqs downloaded"


---------------
for next in $AccList5
do

esearch -db nucleotide -query $next | efetch -db nucleotide -format fasta > USA_seqs_aa.fasta

done
echo "USA subset aa seqs downloaded"

