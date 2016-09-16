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
SET_HUMBLE = set(['bumble', 'fumble', 'humble', 'humbled', 'humbler', 'humbles', 'humbly', 'jumble', 'mumble', 'rumble', 'tumble'])
SET_FIREFLY = set(['direly', 'finely', 'fireclay', 'firefly', 'firmly', 'firstly', 'fixedly', 'freely', 'liefly', 'refly', 'tiredly'])

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


#####################################
# Function that compares the checked word with the word list

def check_spelling(checked_word, dist, word_list):
    """
    Function that iterates through word_list and returns a set of words
    that are within an edit distance dist of the string checked_word.
    """

    # Initialize variables for this function
    _words_found = set()
    _len_checked = len(checked_word)
    _counter = 0

    # Generate the scoring matrix needed to compare the word
    _str_alphabet = "abcdefghijklmnopqrstuvwxyz"
    _alphabet = set(_str_alphabet)
    scoring_matrix = sa.build_scoring_matrix(_alphabet, 2, 1, 0)

    # Iterate through the word list to find the words within distance
    for _word in word_list:
        _counter += 1
        _alignment_matrix = sa.compute_alignment_matrix(checked_word, _word, scoring_matrix)
        if ( _len_checked + len(_word) -
             _alignment_matrix[_len_checked][len(_word)] ) <= dist:
            _words_found.add(_word)
        if _counter % 1000 == 0:
            print "..........", _counter, "words processed."

    return _words_found


#####################################
# Code for answering question 8 of the application

# Read the WordList and print the the first 10 words
word_list = rfs.read_words(WORD_LIST_URL)
print
print "The first 10 words in the word list are:"
for index in range(10):
    print word_list[index]
print

# Check the word "humble" for a edit distance of 1
outcome = check_spelling("humble", 1, word_list)
print
print outcome
if outcome == SET_HUMBLE:
    print "=====> This is the correct selection."
print

# Check the word "firefly" for a edit distance of 2
outcome = check_spelling("firefly", 2, word_list)
print
print outcome
if outcome == SET_FIREFLY:
    print "=====> This is the correct selection."
