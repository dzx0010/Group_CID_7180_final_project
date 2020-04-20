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
 
    output_file = open('nucleotide_counts.tsv','w')
    output_file.write('Gene\tDescription\tA\tC\tG\tT\tLength\tCG%\tOrf_Length\n')
    from Bio import SeqIO
    for cur_record in SeqIO.parse(input_file, "fasta") :
    #count nucleotides in this record...
        gene_name = cur_record.name 
        gene_description = cur_record.description
        A_count = cur_record.seq.count('A')
        C_count = cur_record.seq.count('C')
        G_count = cur_record.seq.count('G')
        T_count = cur_record.seq.count('T')
        length = len(cur_record.seq)
        sequence = cur_record.seq.transcribe()
        genetic_code = {'NAA': 'X', 'NAU': 'X', 'NAC': 'X', 'NAG': 'X', 'NAN': 'X','NCA': 'X', 'NCU': 'X', 'NCC': 'X', 'NCG': 'X', 'NCN': 'X','NUA': 'X', 'NUU': 'X', 'NUC': 'X', 'NUG': 'X', 'NUN': 'X','NGA': 'X', 'NGU': 'X', 'NGC': 'X', 'NGG': 'X', 'NGN': 'X','ANA': 'X', 'ANU': 'X', 'ANC': 'X', 'ANG': 'X', 'ANN': 'X','UNA': 'X', 'UNU': 'X', 'UNC': 'X', 'UNG': 'X', 'UNN': 'X','CNA': 'X', 'CNU': 'X', 'CNC': 'X', 'CNG': 'X', 'CNN': 'X','GNA': 'X', 'GNU': 'X', 'GNC': 'X', 'GNG': 'X', 'GNN': 'X','AAN': 'X', 'AUN': 'X', 'ACN': 'X', 'AGN': 'X', 'NNA': 'X','CAN': 'X', 'CUN': 'X', 'CCN': 'X', 'CGN': 'X', 'NNU': 'X','UAN': 'X', 'UUN': 'X', 'UCN': 'X', 'UGN': 'X', 'NNC': 'X','GAN': 'X', 'GUN': 'X', 'GCN': 'X', 'GGN': 'X', 'NNG': 'X','NNN': 'X', 'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
        longest_peptide =translate.get_longest_peptide(sequence, genetic_code)
        orf_length = len(longest_peptide)
        cg_percentage = float(C_count + G_count) / length
        output_line = '%s\t%s\t%i\t%i\t%i\t%i\t%i\t%f\t%i\n' % \
        (gene_name, gene_description,  A_count, C_count, G_count, T_count, length, cg_percentage, orf_length)
        output_file.write(output_line)
    output_file.close()
    input_file.close()
