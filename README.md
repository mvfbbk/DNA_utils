# DNA_utils

These are a set of scripts that can be helpful in generating oligos for
the study of DNA.

## SplitSeq2KMers

This script is written for python 3.7+ and requires only imports from the
standard python library.

Description:
============

The script will process all FASTA files in the target directory and create
all kmers for a range of sequence lengths from hexamers to 36-mers. The
lower range of the kmers is useful in understanding where random primers
of given lengths will bind within the sequence.
--------------------------------------------------------------------------

Usage:
======

The script needs to be called via it's full path and will act on the
current working directory.

The script produces 2 outputs, a text table that contains the kmer
coordinates and the kmer sequence and a json file that contains this
information in more easily parsable format for finding duplications.
