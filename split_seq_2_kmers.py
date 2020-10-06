"""
Programme:  SplitSeq2KMers
File:       split_seq_2_kmers.py
Version:    Alpha0.1
Date:       2020.10.5
Function:   Obtain all kmers from a given DNA sequence
Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2020
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

--------------------------------------------------------------------------
GPL v3
--------------------------------------------------------------------------
Description:
============
The script will process all FASTA files in the target directory and create
all kmers for a range of sequence lengths from hexamers to 36-mers. The
lower range of the kmers is useful in understanding where random primers
of given lengths will bind within the sequence
--------------------------------------------------------------------------
Usage:
======
This script is written for python 3.7+ and requires only imports from the
stand python library.

The script needs to be called via it's full path and will act on the
current working directory.

The script produces 2 outputs, a text table that contains the kmer
coordinates and the kmer sequence and a json file that contains this
information in more easily parsable format for finding duplications
--------------------------------------------------------------------------
Revision History:
=================
A0.1    05.10.20    Alpha   By: MVF
"""

#!/usr/bin/env python3
import os
import glob
import json

# Set working directory and find all sequence file in the directory
path = os.getcwd() + "/{}"
file_list = glob.glob('*.fasta')

# Define ramge of kmers to be found, up to 35 cyles of sequencing
k_range = range(6, 36, 1)

# Itterate over a number of reference fasta files
for f in file_list:
    f_name = f.split('.')[0]
    with open(path.format(f), 'r') as reference:
        # Skip first line as this is the FASTA header
        ref = reference.readlines()[1:]
        # FASTA files can be multi-line, ensure that any newline characters are removed
        ref = ''.join(ref).strip().replace('\n','')
        # Loop through kmer lengths to determine the kmers
        for k_len in k_range:
            list_of_kmers = []
            list_of_kmer_starts  = []
            list_of_kmer_ends = []
            kmers_entry = {}
            # Pick kmers
            for i in range(0, len(ref)-k_len+1):
                ref = list(ref)
                start = i + 1
                end = start + k_len
                kmer = ''.join(ref[start : end])
                kmers_entry[(start)] = kmer
                # Write kmers to txt and json files
                with open(path.format(f'{f_name}_{k_len}-mer_list.txt'), 'a') as outfile:
                    outfile.write(f'{start}:{end}, {kmer}\n')
            with open(path.format(f'{f_name}_{k_len}-mers.json'), 'w') as outjson:
                outjson.write(json.dumps(kmers_entry, sort_keys = True, indent = 2))
