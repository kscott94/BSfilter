BSfilter is a python3 script that takes at lease one argument and at most 3 arguments.

Its purpose is to take in a fastq file and output a fastq file from the original that contain reads with a specified frequency and/or counts of Cytosines per read.

This python script uses the python package biopython and as such biopython dependencies.

BSfilter can be run from the command line using the following syntax:

python3 BSfilter.py -fq <path/to/fastq/file> [-options]

options:
-fq <string>    path/to/fastq/file.

-mC <float>    max frequency of Cytosines per read allowed through filter. Default is 1.0

--count <integer>    max number of Cytosones per read allowed through filter. Default is 1000
  
  
Future updates will include fasta input option as well as various filtering parameters.
