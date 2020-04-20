#!/usr/bin/env python3

from Bio.Align.Applications import ClustalOmegaCommandline 
#define input file
in_file = "China_seqs.fasta"

# define output file (I have tried just adding .phylip or no .format)
out_file = "out_China_seqs.phylip"

# get the command for Clustal Omega
# what I tried and what should work: outfmt = phylip
clustalomega_cline = ClustalOmegaCommandline(infile = in_file, outfile = out_file, verbose = True, auto = False)

# print the executable command
print(clustalomega_cline)

# The commandline will prompt you at this point to enter the line calling to your file, it should have this format:
# ./clustal-omega-1.2.3-macosx -i in_filename.fasta -o in_filename.phylip --auto -v
