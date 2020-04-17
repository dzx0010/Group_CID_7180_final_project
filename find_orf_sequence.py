#!usr/bin/env python3
import sys
import translate
def parse_sequence_from_path(path):
    # Try to open the path to read from it, and handle exceptions if they
    # arrise
    try:
        input_file = open(path, 'r')
    except FileNotFoundError as e:
        sys.stderr.write("Sorry, couldn't find path {}".format(path))
        raise e
    except IsADirectoryError as e:
        sys.stderr.write("Sorry, path {} appears to be a directory".format(
                path))
        raise e
    except:
        sys.stderr.write("Sorry, something went wrong when trying to open {}".format(
                path))
        raise

    output_file = open('longest_peptide.fasta','w')
    from Bio import SeqIO
    for cur_record in SeqIO.parse(input_file, "fasta") :
    #count nucleotides in this record...
        gene_name = cur_record.name
        gene_description = cur_record.description
        sequence = cur_record.seq.transcribe()
        genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
        longest_peptide =translate.get_longest_peptide(sequence, genetic_code)
        length = len(longest_peptide)
        output_line = '%s\t%s\t%i\n' % \
        (gene_name, gene_description, length)
        longest_peptide = '%s\n' % (longest_peptide)
        output_file.write('>'+ output_line)
        output_file.write(longest_peptide)
    output_file.close()
    input_file.close()


