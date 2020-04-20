#!/bin/bash

#Run script and enter the name of a txt file with locations + accessions
#tail command will cut off title line
#awk prints only accessions, tr changes them from vertical list to comma-separated
#sed removes last comma from list
#final file is (usually) DL_[blah]_sorted.txt


#cat $# | tr "\n" "," | sed 's/,$//'

echo "Enter accession file name: "
read var1

tail -n +2 $var1 > $var1.tmp

awk -F ";" '{print $2}' $var1.tmp | tr "\n" "," | sed 's/,$//' > DL_$var1

rm $var1.tmp

echo "accession list converted"

