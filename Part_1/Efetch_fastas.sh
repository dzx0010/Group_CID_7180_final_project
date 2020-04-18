#!/bin/bash

module load ncbi-toolkit

for Var in 'Test_format.txt'
do
efetch -db genome -format fasta "$Var"
echo "$Var downloaded" >> DL_record.txt
date >> DL_record.txt

#Error response:
#Entrez Direct does not support positional arguments.
#Please remember to quote parameter values containing
#whitespace or shell metacharacters.


done
