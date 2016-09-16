"""
Code developed for application #4 question 4 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import urllib2
import random
import matplotlib.pyplot as plt
import alignments_read_functions as rfs
import sequence_alignment as sa

# URLs for the data files used in the application
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


##############################################################
# Function to generate a scoring distibution of trails to align a random generated
# sequence with a provided second sequence

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Function that takes as input two sequences seq_x and seq_y, a scoring matrix,
    and a number of trials num_trials. This functions returns a dictionary
    scoring_distribution that represents an un-normalized distribution generated
    by performing a local alignment process num_trials times.
    """

    # Initialize variables used in this function
    _scoring_distribution = {}
    _trials_to_go = num_trials
    _rand_y = seq_y

    while _trials_to_go > 0:
        # Create a random permutation of the sequence seq_y
        _lst_rand_y = list(_rand_y)
        random.shuffle(_lst_rand_y)
        _rand_y = ""
        for _char in _lst_rand_y:
            _rand_y += _char
        
        # Compute the maximum score for the local alignment of seq_x and rand_y
        _alignment_matrix = sa.compute_alignment_matrix(seq_x, _rand_y, scoring_matrix, False)
        _num_rows = len(_alignment_matrix)
        _num_cols = len(_alignment_matrix[0])
        _max_score = -1
        for _index1 in range(_num_rows):
            for _index2 in range(_num_cols):
                if ( _alignment_matrix[_index1][_index2] > _max_score ):
                    _max_score = _alignment_matrix[_index1][_index2]

        # Count the scores generated in the dictionary scoring_distribution
        _scoring_distribution[_max_score] = _scoring_distribution.get(_max_score, 0) + 1
        if ( num_trials - _trials_to_go + 1 ) % 1 == 0:
            print ".......... Trial", ( num_trials - _trials_to_go + 1 ), "completed."
        _trials_to_go -= 1

    return _scoring_distribution


#####################################
# Code for answering question 4 of the application

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

# Compute the scoring distribution and write the result into a csv-file
scoring_distribution = generate_null_distribution(human_protein, fruitfly_protein, scoring_matrix, 1000)
print scoring_distribution

# Write the scoring distibution into the file scoring_dist.txt
fhandle = open("scoring_dist.txt", "w")
for score, number in scoring_distribution.items():
    out = str(score) + " " + str(number) + "\n"
    fhandle.write(out)
fhandle.close()    

# Generate the normalized version of the distribution in the lists needed for the plot
x_axis = []
y_axis = []
total = 0
for score, number in scoring_distribution.items():
    x_axis.append(score)
    y_axis.append(number)
    total += number
total = float(total)
for index in range(len(y_axis)):
    y_axis[index] /= total

# Create a plot of the result
plt.bar(x_axis, y_axis)
plt.grid(False)
plt.title("Plot 17: bar plot of the null scoring distribution")
plt.xlabel("score")
plt.ylabel("fraction of trials")
plt.show()
