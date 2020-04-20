#!/bin/bash
module load clustal_omega/1.2.4
clustalo -i /mnt/beegfs/home/aubcls65/final_project/Group_Kcd_7180/longest_peptide.fasta\
 -o /mnt/beegfs/home/aubcls65/final_project/Group_Kcd_7180/orf_translate.aln --outfmt=clu --force
clustalo -i /mnt/beegfs/home/aubcls65/final_project/Group_Kcd_7180/example_sequence.fasta\
 -o /mnt/beegfs/home/aubcls65/final_project/Group_Kcd_7180/nucleotide_sequence.aln --outfmt=clu --force


