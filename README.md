# DNA_utils

These are a set of scripts that can be helpful in generating oligos for
the study of DNA.

## SplitSeq2KMers

This script is written for python 3.7+ and requires only imports from the
standard python library.

### Description:

The script will process all FASTA files in the target directory and create
all kmers for a range of sequence lengths from hexamers to 36-mers. The
lower range of the kmers is useful in understanding where random primers
of given lengths will bind within the sequence.


### Usage:

The script needs to be called via it's full path and will act on the
current working directory.

The script produces 2 outputs, a text table that contains the kmer
coordinates and the kmer sequence and a json file that contains this
information in more easily parsable format for finding duplications.

## KMerGenerator

This script is written for python 3.7+ and requires only imports from the
standard python library.

### Description:

The script uses a character alphabet to generate kmers of a given length
for that alphabet. The itertools product function will create every unique
string value for the combination of alphabet and kmer length. with
increased kmer length memory usage becomes too intensive to be able to
handle this all in memory. To overcome this the script will write each new
kmer to file.

Perfomance is slow at higher kmer lengths but the process is able to run
effectively drawing few system resources.

The intended purpose of this script is the automated generation of sequences
which may have the potential to be synthesised in to molecular biology primers.
These could be used in a number of applications or fed into a primer design
process that could match the sequnences to specific target sites within a genome.
This is an alternative and more general process to the SplitSeq2KMers mentioned
above.

### Usage:

The script has been set up with default parameters of a DNA alphabet and a kmer
length of 18, which is the minimum recommended PCR primer length to ensure
specificity, it can be called directly with these defaults to generate the
68.7*10e9 unique combinations or the script can be used as a module and the
function called within a separate main script with user-defined parameters
