#!/bin/bash



#Print 2 useful columns to temp file

awk -F "," '{print $6";"$1}' COVID_Seqs.csv > Temp_Accessions.txt 

#remove " from country names

cat Temp_Accessions.txt | tr -d '"' > Accessions_COVID.txt

#rm Temp_Accessions.txt

echo "List ready to sort"

#sort based on country
#sort -d --sort="China" -o China_sorted.txt COVID_Seqs.csv

#grep for each country
grep -e "China" Accessions_COVID.txt > China_sorted.txt
#sort -R China_sorted.txt > China_random_sorted.txt
#grep -e "China:" Accessions_COVID.txt > China_sites_sorted.txt
echo "China sorted"


grep -e "USA" Accessions_COVID.txt > USA_sorted.txt

#grep -e "USA:" Accessions_COVID.txt > USA_states_sorted.txt

###USA has >700 samples from various locations.  For detailed comparison
###one can separate states/regions as done in later scripts.
###For test purposes we will randomize the US Accessions and download 100 of them

sort -R USA_sorted.txt > USA_random_sorted.txt

split -l 100 USA_random_sorted.txt USA_randsplit_

echo "USA sorted"

grep -f Euro_Countries.txt Accessions_COVID.txt > Euro_sorted.txt
echo "Euro sorted"

grep -f Asia_Countries.txt Accessions_COVID.txt > Asia_sorted.txt
echo "Asia sorted"

grep -f Other_countries.txt Accessions_COVID.txt > Other_sorted.txt 
echo "Remainder sorted"

echo "-------------------------------"

#echo *_sorted.txt > Sorted_files.txt

#FILELIST=`cat Sorted_files.txt`
#For FILE in $FILELIST
#do 
###randomize locations in each file
#sort -u -R $FILE 

#cut country from each list
 
#cut -f 2 -d ';' $FILE
#done
#echo "Sorted list of accessions ready"

