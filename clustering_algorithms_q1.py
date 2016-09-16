"""
Code developed for application #3 question 1 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import random
import time
import alg_cluster as cl
import alg_project3_solution as sol
import matplotlib.pyplot as plt

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Function that generates random clusters for the analyses

def gen_random_clusters(num_clusters):
    """
    Function that generates num_clusters clusters placed randomly in the
    square spacewith corners (+/- 1.0, +/- 1.0).
        
    Returns a list of num_clusters clusters
    """
    _cluster_list = []
    for _index in range(num_clusters):
        _horiz_pos = random.random() * 2.0 - 1.0
        _vert_pos = random.random() * 2.0 - 1.0
        _new_cluster = cl.Cluster(set([]), _horiz_pos, _vert_pos, 1, 1)
        _cluster_list.append(_new_cluster)
    
    return _cluster_list


#####################################
# Code for answering question 1 of the application

# Measure the running times for the functions slow_closest_pair and fast_closest_pair
num_clusters = []
running_times_slow = []
running_times_fast = []
for index in range(2,201):
    cluster_list = gen_random_clusters(index)
    num_clusters.append(index)
    start_time = time.time()
    distance = sol.slow_closest_pair(cluster_list)
    end_time = time.time()
    running_times_slow.append(end_time - start_time)
    start_time = time.time()
    distance = sol.fast_closest_pair(cluster_list)
    end_time = time.time()
    running_times_fast.append(end_time - start_time)
    if index % 10 == 0:
        print "=====> Covered clusterlist up to", index
    
# Create plot of the result
plt.plot(num_clusters, running_times_slow, '-b', label='slow_closest_pair')
plt.plot(num_clusters, running_times_fast, '-r', label='fast_closest_pair')
plt.legend(loc='upper left')
plt.grid(True)
plt.title("Plot 9: running times of slow_closest_pair and fast_closest_pair")
plt.xlabel("number of clusters processed")
plt.ylabel("runnning time (sec.)")
plt.show()
