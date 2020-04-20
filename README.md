# Xing_7180
# install packages
1.  Set up running environment and install software:
(1) Modify shebang line of setup.py to make it run correctly
(2) $Python3 setup.py build    to build environment 
(3) $python3 setup.py install  to install software needed
(4) $python3 setup.py - - help  can help you run  
2. if not install successfully you can try pip install Run the below from within your $HOME directory on the ASC!!

Use python3 to install pip (a python package/library manager) in your user account
using a python script copied from the biobootcamp directory

cp ~/biobootcamp/get-pip.py . && python3 get-pip.py --user

Confirm that pip is running in your user account and its version is 20.0.2

.local/bin/pip --version

Now we need to add the ~/.local/bin to our $PATH, so....

nano ~/.bashrc.local

And add the following to the bottom of the file (what's the reason for the below?)

export PATH=~/.local/bin:$PATH

Now log out and back into your supercomputer account to pick up the new $PATH. To make sure this is the case,

echo $PATH

And be sure the new ~/.local/bin is at the beginning of your $PATH

Now time to use pip to install packages like:

pip install biopython

# Download genome sequence
 Download  all complete genomes with fasta format from NCBI:
https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049&SLen_i=29000%20TO%2030000
# data preparation
replace non ATCG by N.
sed -e '/^[^>]/s/[^ATGCatgc]/N/g' example_sequence.fasta > example_sequence_processed.fasta

#Run CID.py
You can run with command line:
python3 CID.py sequences4_14_2020.fasta_processed.fasta
but it will take a long time.
you can use script CID.sh

