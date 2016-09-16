"""
Code developed for application #4 question 2 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import urllib2
import alignments_read_functions as rfs
import sequence_alignment as sa

# URLs for the data files used in the application
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"

# Resulting local alignments from question 1
HUMAN_LOCAL = "HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ"
FRUITFLY_LOCAL = "HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ"

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


#####################################
# Code for answering question 2 of the application

# Read the ConsensusPAXDomain and print the result
consensus_pax = rfs.read_protein(CONSENSUS_PAX_URL)
print "Consensus PAX domain protein:"
print consensus_pax
print "Length consensus PAX domain protein =", len(consensus_pax)
print

# Read the PAM50 scoring matrix and print the result
scoring_matrix = rfs.read_scoring_matrix(PAM50_URL)

# Computations for the human protein sequence
# . remove all '-' from the sequence
lst_of_strings = HUMAN_LOCAL.split('-')
human_local = ""
for substring in lst_of_strings:
    human_local += substring
# . compute the alignment between this sequence and the ConsensusPAXDomain sequence
alignment_matrix = sa.compute_alignment_matrix(human_local, consensus_pax, scoring_matrix)
global_alignment = sa.compute_global_alignment(human_local, consensus_pax, scoring_matrix, alignment_matrix)
# . determine percentage of agreement
agreements = 0
for index in range(len(global_alignment[1])):
    if global_alignment[1][index] == global_alignment[2][index]:
        agreements += 1
print ">>>>>>>>>>>>>>> Percentage of agreement human local    =", ( float(agreements) / len(global_alignment[1]) ) * 100, "%" 

# Computations for the fruitfly protein sequence
# . remove all '-' from the sequence
lst_of_strings = FRUITFLY_LOCAL.split('-')
fruitfly_local = ""
for substring in lst_of_strings:
    fruitfly_local += substring
# . compute the alignment between this sequence and the ConsensusPAXDomain sequence
alignment_matrix = sa.compute_alignment_matrix(fruitfly_local, consensus_pax, scoring_matrix)
global_alignment = sa.compute_global_alignment(fruitfly_local, consensus_pax, scoring_matrix, alignment_matrix)
# . determine percentage of agreement
agreements = 0
for index in range(len(global_alignment[1])):
    if global_alignment[1][index] == global_alignment[2][index]:
        agreements += 1
print ">>>>>>>>>>>>>>> Percentage of agreement fruitfly local =", ( float(agreements) / len(global_alignment[1]) ) * 100, "%" 

