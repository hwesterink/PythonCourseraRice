"""
Code developed for application #4 question 5 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import math


#####################################
# Outcome s for question 1

S_Q1 = 875

#####################################
# Code for the statistical analysis of question 5 of the application

# Read the scoring distibution from the file scoring_dist.txt and compute the averige
fhandle = open("scoring_dist.txt")
scores = []
counts = []
trials = 0
total = 0
for line in fhandle:
    line_list = line.split(' ')
    line_score = int(line_list[0])
    line_count = int(line_list[1])
    scores.append(line_score)
    counts.append(line_count)
    total += line_score * line_count
    trials += line_count
    
trials = float(trials)
mean = total / trials
print "mean               =", mean

# Compute the standard deviation
deviation_counter = 0
for index in range(len(scores)):
    deviation_counter += ((scores[index] - mean) **2) * counts[index]
deviation_squared = deviation_counter / trials
standard_deviation = math.sqrt(deviation_squared)
print "standard deviation =", standard_deviation

# Compute the z-score
z_score = ( S_Q1 - mean ) / standard_deviation
print "z-score            =", z_score
