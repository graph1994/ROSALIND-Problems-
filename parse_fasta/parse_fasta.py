__author__ = 'graphite'

#Script made to deal with reading Fasta Files.
#It requires a file name and it reads that file breaking it down at each record.
# Saves records as Dictonary with Record Id as Key and item as Base pairs.

def parse_fasta(file):
    data = open(file).readlines()
    records = {}
    record_id = 0
    for line in data:

        if line.startswith('>'):
            record_id = line[1:].rstrip()
            records[record_id] = ''
        else:
            records[record_id] += line.rstrip()
    return records