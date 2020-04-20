#! /usr/bin/env python3

import sys

def translate_sequence(rna_sequence, genetic_code):
    amino_acids = ""
    rna_sequence = rna_sequence.upper()
    if len(rna_sequence) < 3:
        return ''
    else:
        for i in range(0,len(rna_sequence)-2,3):
            codon = rna_sequence[i:i+3]
            if genetic_code[codon] == '*':
                break
            amino_acids+= genetic_code[codon]
    return amino_acids
    """Translates a sequence of RNA into a sequence of amino acids.
    Translates `rna_sequence` into string of amino acids, according to the
    `genetic_code` given as a dict. Translation begins at the first position of
    the `rna_sequence` and continues until the first stop codon is encountered
    or the end of `rna_sequence` is reached.

    If `rna_sequence` is less than 3 bases long, or starts with a stop codon,
    an empty string is returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    str
       A string of the translated amino acids.
    """
    

def get_all_translations(rna_sequence, genetic_code):
    sequence = rna_sequence.upper()
    num_bases = len(sequence)-3
    amino_acid_list = []
    for a in range(num_bases+1):
        start = sequence[a:a+3]
        if start == 'AUG':
            rna_seq = sequence[a:]
            amino_acid_all= ""
            for b in range(0,len(rna_seq)-2, 3):
                new = rna_seq[b:b+3]
                if genetic_code[new]== '*':
                    break
                amino_acid_all+= genetic_code[new]
            amino_acid_list.append(amino_acid_all)
    return amino_acid_list
    
    """Get a list of all amino acid sequences encoded by an RNA sequence.

    All three reading frames of `rna_sequence` are scanned from 'left' to
    'right', and the generation of a sequence of amino acids is started
    whenever the start codon 'AUG' is found. The `rna_sequence` is assumed to
    be in the correct orientation (i.e., no reverse and/or complement of the
    sequence is explored).

    The function returns a list of all possible amino acid sequences that
    are encoded by `rna_sequence`.

    If no amino acids can be translated from `rna_sequence`, an empty list is
    returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    list
        A list of strings; each string is an sequence of amino acids encoded by
        `rna_sequence`.
    """
    

def get_reverse(sequence):
    sequence = sequence.upper()
    if len(sequence)> 0:
        return ''.join(reversed(sequence))
    else:
        return ''
    """Reverse orientation of `sequence`.

    Returns a string with `sequence` in the reverse order.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> get_reverse('AUGC')
    'CGUA'
    >>> get_reverse('ATGC')
    'CGTA'
    """
    

def get_complement(sequence):
    sequence = sequence.upper()
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A', 'N': 'N'} 
    if len(sequence)> 0:
        return ''.join(complement[base] for base in sequence)
    else:
        return ''

    """Get the complement of a `sequence` of nucleotides.

    Returns a string with the complementary sequence of `sequence`.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> get_reverse('AUGC')
    'UACG'
    >>> get_reverse('ATGC')
    'TACG'
    """
    

def reverse_and_complement(sequence):
    sequence = sequence.upper()
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A',  'N': 'N'}
    if len(sequence)> 0:
        return ''.join(complement[base] for base in sequence[::-1])
    else:
        return ''
    """Get the reversed and complemented form of a `sequence` of nucleotides.

    Returns a string that is the reversed and complemented sequence
    of `sequence`.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> reverse_and_complement('AUGC')
    'GCAU'
    >>> reverse_and_complement('ATGC')
    'GCAT'
    """
    

def get_longest_peptide(rna_sequence, genetic_code):
    RNA = rna_sequence.upper()
    reverse_se = reverse_and_complement(RNA)
    if len(translate_sequence(reverse_se, genetic_code)) == 0 or len(translate_sequence(RNA, genetic_code)) == 0:
        return ''
    else:
        c = 0
        RNA_amino = ''
        while  c < 4:
            for f in range(len(RNA)-2):
                RNA_start = RNA[f:f+3]
                if RNA_start == 'AUG':
                    RNA_new = RNA[f:]
                    if len(RNA_amino) < len(translate_sequence(RNA_new, genetic_code)):
                        RNA_amino = translate_sequence(RNA_new, genetic_code)
            for e in range(len(reverse_se)-2):
                reverse_start = reverse_se[e:e+3]
                if reverse_start == 'AUG':
                    reverse_new = reverse_se[e:]
                    if len(RNA_amino) < len(translate_sequence(reverse_new, genetic_code)):
                        RNA_amino = translate_sequence(reverse_new, genetic_code)
            c=c+1
            return RNA_amino 

    """Get the longest peptide encoded by an RNA sequence.

    Explore six reading frames of `rna_sequence` (the three reading frames of
    `rna_sequence`, and the three reading frames of the reverse and complement
    of `rna_sequence`) and return (as a string) the longest sequence of amino
    acids that it encodes, according to the `genetic_code`.

    If no amino acids can be translated from `rna_sequence` nor its reverse and
    complement, an empty string is returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    str
        A string of the longest sequence of amino acids encoded by
        `rna_sequence`.
    """
    


if __name__ == '__main__':
    genetic_code = {'NAA': 'X', 'NAU': 'X', 'NAC': 'X', 'NAG': 'X', 'NAN': 'X', 'NCA': 'X', 'NCU': 'X', 'NCC': 'X', 'NCG': 'X', 'NCN': 'X', 'NUA': 'X', 'NUU': 'X', 'NUC': 'X', 'NUG': 'X', 'NUN': 'X', 'NGA': 'X', 'NGU': 'X', 'NGC': 'X', 'NGG': 'X', 'NGN': 'X', 'ANA': 'X', 'ANU': 'X', 'ANC': 'X', 'ANG': 'X', 'ANN': 'X', 'UNA': 'X', 'UNU': 'X', 'UNC': 'X', 'UNG': 'X', 'UNN': 'X', 'CNA': 'X', 'CNU': 'X', 'CNC': 'X', 'CNG': 'X', 'CNN': 'X', 'GNA': 'X', 'GNU': 'X', 'GNC': 'X', 'GNG': 'X', 'GNN': 'X', 'AAN': 'X', 'AUN': 'X', 'ACN': 'X', 'AGN': 'X', 'NNA': 'X', 'CAN': 'X', 'CUN': 'X', 'CCN': 'X', 'CGN': 'X', 'NNU': 'X', 'UAN': 'X', 'UUN': 'X', 'UCN': 'X', 'UGN': 'X', 'NNC': 'X', 'GAN': 'X', 'GUN': 'X', 'GCN': 'X', 'GGN': 'X', 'NNG': 'X', 'NNN': 'X', 'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
    rna_seq = ("AUG"
            "UAC"
            "UGG"
            "CAC"
            "GCU"
            "ACU"
            "GCU"
            "CCA"
            "UAU"
            "ACU"
            "CAC"
            "CAG"
            "AAU"
            "AUC"
            "AGU"
            "ACA"
            "GCG")
    longest_peptide = get_longest_peptide(rna_sequence = rna_seq,
            genetic_code = genetic_code)
    assert isinstance(longest_peptide, str), "Oops: the longest peptide is {0}, not a string".format(longest_peptide)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
            rna_seq,
            longest_peptide)
    sys.stdout.write(message)
    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
