#!/bin/bash

#First echo the csv contents
#then split into location files based on awk conditional
#if $6= china then print $1 to China_accessions
#else if $6 = USA then print $1 to USA_accessions, etc
#later we will use head to get top 10 of each set
#and hope that works

for Line in COVID_seqs.csv 
do
    if $6 == 'China*' 
    then
        echo $1 >> China_accessions.txt

    elif $6 == 'USA*'
    then
        echo $1 >> USA_accessions.txt
    
    else
        echo $1 >> Other_accessions.txt
    fi
done


