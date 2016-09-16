"""
Code developed for application #4 question 1 of the course
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

# Results from the solution page to check the computed local alignment
HUMAN_RESULT = "HSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATPEVVSKIAQYKRECPSIFAWEIRDRLLSEGVCTNDNIPSVSSINRVLRNLASEK-QQ"
FRUITFLY_RESULT = "HSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRYYETGSIRPRAIGGSKPRVATAEVVSKISQYKRECPSIFAWEIRDRLLQENVCTNDNIPSVSSINRVLRNLAAQKEQQ"

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


##############################################################
# Helper functions to print the scoring and the alignment matrix

def print_scoring_matrix(scoring_matrix):
    """
    Helper function that prints out a scoring_matrix
    """

    chars = ""
    for char, value in scoring_matrix.items():
        chars += char
    print "Scoring matrix for:", chars
    for index in range(len(chars)):
        print "For row", chars[index], "=====>", scoring_matrix[chars[index]]


def print_alignment_matrix(alignment_matrix, seq_x, seq_y):
    """
    Helper function that prints out the alignment_matrix
    """

    row_names = "0" + seq_x
    print "Alignment matrix where columns are: 0" + seq_y
    for index in range(len(seq_x)+1):
        print "For row", row_names[index], "=====>", alignment_matrix[index]
        

#####################################
# Code for answering question 1 of the application

# Read the HumanEyelessProtein and print the result
human_protein = rfs.read_protein(HUMAN_EYELESS_URL)
print "Human protein:"
print human_protein
print "Length human protein =", len(human_protein)
print
    
# Read the FruitflyEyelessProtein and print the result
fruitfly_protein = rfs.read_protein(FRUITFLY_EYELESS_URL)
print "Fruitfly protein:"
print fruitfly_protein
print "Length fruitfly protein =", len(fruitfly_protein)
print
    
# Read the PAM50 scoring matrix and print the result
scoring_matrix = rfs.read_scoring_matrix(PAM50_URL)
#print_scoring_matrix(scoring_matrix)
#print
    
# Compute local alignment matrix for the two proteins
alignment_matrix = sa.compute_alignment_matrix(human_protein, fruitfly_protein, scoring_matrix, False)
#print_alignment_matrix(alignment_matrix, human_protein, fruitfly_protein)
#print

# Compute and print local alignment
local_alignment = sa.compute_local_alignment(human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
print
print "==================> Local alignment:"
print ".......... Local alignment score:    ", local_alignment[0]
print ".......... Human protein sequence:   ", local_alignment[1]
if local_alignment[1] == HUMAN_RESULT:
    print ">>>>>>>>>>>>>>>>>>>> THIS IS THE RIGHT SEQUENCE"
print ".......... Fruitfly protein sequence:", local_alignment[2]
if local_alignment[2] == FRUITFLY_RESULT:
    print ">>>>>>>>>>>>>>>>>>>> THIS IS THE RIGHT SEQUENCE"
print ".......... Length aligned sequence:  ", len(local_alignment[1])
