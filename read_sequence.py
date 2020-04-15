#!usr/bin/env python3

from itertools import groupby

def read_seq(sequence):
    faiter = (x[1] for x in groupby(sequence, lambda l:l[0] == ">"))
    for header in faiter:
        header = next(header)[1:].strip()
        seq = "".join(s.strip() for s in next(faiter))
        seq = seq.replace('T', 'U')
        print(seq)

