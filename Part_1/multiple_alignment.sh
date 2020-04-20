#!/bin/bash
module load clustal_omega/1.2.4
clustalo -i ~/Part_1/China_seqs.fasta\
 -o ~/Part_1/China_seqs.aln --outfmt=clu --force
clustalo -i ~/Part_1/USA_seqs.fasta\
-o ~/Part_1/USA_seqs.aln --outfmt=clu --force


