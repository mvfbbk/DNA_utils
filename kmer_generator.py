"""
Programme:  KMerGenerator
File:       kmer_generator.py
Version:    Alpha0.1
Date:       2020.10.5
Function:   Generate KMers of specific lengths from a dictionary of
            possible characters
Copyright:  (c) Matthieu Vizuete-Forster, BBK, 2020
Author:     Matthieu Vizuete-Forster
Address:    Department of Biological Sciences
            Malet Steet, London, WC1E 7HX

---------------------------------------------------------------------------
GPL v3
---------------------------------------------------------------------------
Description:
============
The script uses a character alphabet to generate kmers of a given length
for that alphabet. The itertools product function will create every unique
string value for the combination of alphabet and kmer length. with
increased kmer length memory usage becomes too intensive to be able to
handle this all in memory. To overcome this the script will write each new
kmer to file.
Perfomance is slow at higher kmer lengths but the process is able to run
effectively drawing few system resources.
---------------------------------------------------------------------------
Usage:
======
This script is written for python 3.7+ and requires only imports from the
stand python library.

The script needs to be called via it's full path and will act on the
current working directory.

The script produces 1 output, a text file which contains each created kmer
sequence, one per line
---------------------------------------------------------------------------
Revision History:
=================
A0.1    05.10.20    Alpha   By: MVF
A0.2    08.10.20    Alpha   By: MVF    Comment: replaced random selection
                                                from alphabet with
                                                itertools.product()
                                                instigating writing to
                                                disc at each cycle for more
                                                efficient memory usage with
                                                longer kmer values
"""

import os
import itertools

def generate_kmers(polymer, kmer_length):

    # Set working parameters
    path = os.getcwd() + "/{}"

    # Check which type of polymer is required
    if str.upper(polymer) == 'DNA':
        alphabet = "ATCG"
    elif str.upper(polymer) == 'RNA':
        alphabet = "AUCG"
    elif str.lower(polymer) == 'protein':
        alphabet = "GALMFWKQESPVICYHRNDT"
    else:
        raise ValueError('Incorrect polymer type defined. Accepted vales are DNA, RNA or protein')

    # Create output file to reduce memory usage that would be needed for higher kmer lengths
    with open(path.format(f'{kmer_length}_kmer_unique_list.txt'), 'a') as outfile:
        # Generate the kmers, will produce all possible permutations of the alphabet of lenth kmer_length
        for output in itertools.product(alphabet, repeat=kmer_length):
            # write each generated kmer to file
            outfile.write(''.join(output) + '\n')

if __name__ == '__main__':
    # Most DNA PCR primers will be at least 18 bases long
    # this should produce ~68.7*10e9 unique combinations of sequences
    generate_kmers('DNA',18)
