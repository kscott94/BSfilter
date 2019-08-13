#!/usr/bin/env python3

import argparse
import os
import datetime
from Bio import SeqIO   #pacakge from biopython

parser = argparse.ArgumentParser()
parser.add_argument('-fq', type=str) # path/to/fastq/file
parser.add_argument('-mC', type=float, default=1.0)    # methyl cytosine frequency allowed per read
parser.add_argument('--count', type=int, default=1000)  # methyl cytosine count allowed per read

args = parser.parse_args()

print('BSfilter version 1.0\n')
start_time = datetime.datetime.now()
print("started at: " + str(start_time))

with open(args.fq, "rU") as handle:
    """split fastq file name into its parts"""
    fq_name, fq_ext = os.path.splitext(args.fq)

    """print basic information about fastq file"""
    read_count = len(list(SeqIO.parse(args.fq, "fastq")))
    print("Found %i records in %s" % (read_count, args.fq))

        """Make sequence uppercase"""
        record.seq = record.seq.upper()

        """Assign variables for filter"""
        record.seq = record.seq.upper()
        mC_count = record.seq.count("C")
        N_count = len(record.seq)
        mC_persistence = float(mC_count / N_count)

        """define filter and print to file"""
        new_fq_name = fq_name + "_filtered" + fq_ext
        record_sequence = str(record.seq)

        if mC_persistence <= args.mC and mC_count <= args.count:
            with open(new_fq_name, 'a') as f_filter_out:
                f_filter_out.write(record.format("fastq"))

with open(new_fq_name, 'r') as filtered_fq:
    read_count2 = len(list(SeqIO.parse(filtered_fq, "fastq")))
    print("Found %i records in %s" % (read_count2, new_fq_name))

end_time = datetime.datetime.now()
print("finished at: " + str(end_time))
