Welcome to our pipeline for analysis of COVID-19 sequences.

We are starting with the file COVID_Seqs.csv as a reference for accession numbers.

The first step will be to sort the accessions by country for comparison.
SortCut_filter.sh will copy the location and accession data to a separate file,
then copy out accessions from different countries.

--------------outline version-----------
Step 1
Start with COVID_Seqs.csv
Run SortCut_Filter.sh to separate seqs into lists of “location; accession” ($place_sorted.txt)
--also splits up USA into sets of 100 randomized (USA_randsplit_aa)

ls *_sorted* for reference

Run Lines_to_commas.sh to convert location/accession lists to comma-separated lists for download use
Ls DL* for reference

Run Collect_seqs.sh and input name of your DL file to get fasta
Ls -thor *.fasta to make sure it went through

If size seems too big or small, check number of samples with:
cat Other_seqs.fasta | grep ">" | wc –l

