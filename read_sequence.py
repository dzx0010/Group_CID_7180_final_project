#!usr/bin/env python3
import sys
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
    output_file.write('Gene\tA\tC\tG\tT\tLength\tCG%\n')
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
        cg_percentage = float(C_count + G_count) / length
        output_line = '%s\t%s\t%i\t%i\t%i\t%i\t%i\t%f\n' % \
        (gene_name, gene_description,  A_count, C_count, G_count, T_count, length, cg_percentage)
    output_file.write(output_line)
    output_file.close()
    input_file.close()
