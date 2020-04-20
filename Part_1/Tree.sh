#!/bin/bash
####################################STEP 1#####################################
module load clustal_omega/1.2.4
####################################STEP 2#####################################
##Clustalw is used to align the DNA sequences 
#and create an outputfile for estimating the tree
#Make sure clustalw is installed
#if not, type 'clustalw' in the command line and follow instructions

clustalo -INFILE=China_seqs.fasta -TYPE=DNA -OUTFILE=out_all_China_seqs.phy -OUTPUT=PHYLIP

####################################STEP 3######################################
##Phyml estimates the most suitable tree.
#Make sure phyml is installed.
#If not, install by typing 'phyml' in the command line and follow instructions.
phyml -i out_all_China_seqs.phy -d nt -n 1 -m HKY85

####################################STEP 4######################################
##Plotting and saving the tree with R (go to Rscript)
Rscript plotTree.r
