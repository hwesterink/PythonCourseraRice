"""
Code developed for application #2 question 3 of the course
Algorithmic Thinking I
"""

# Imports needed for this code
import time
import connections_analysis as ca
import network_analysis_gen as nagen
import matplotlib.pyplot as plt

# CodeSkulptor imports (only if this code is run in Code Skulptor)
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(20)


#####################################
# Code for answering question 3 of the application

# Initialize the list for the plot
num_nodes = [0]
time_targeted_order = [0.0]
time_fast_targeted_order = [0.0]

# Generate all the point for the plot
for nodes in range(10, 1000, 10):
    # Fill in the nodes
    num_nodes.append(nodes)
    # Generate the graph to be used
    print "=====> Generating graph with", nodes, "nodes."
    UPA_graph = nagen.make_graph_UPA(nodes, 5)
    # Measure the time for targeted_order
    print
    print "=====> Run targeted_order for", nodes, "nodes."
    start_time = time.time()
    attack_list = nagen.targeted_order(UPA_graph)
    end_time = time.time()
    time_targeted_order.append(end_time - start_time)
    # Measure the time for fast_targeted_order
    print
    print "=====> Run fast_targeted_order for", nodes, "nodes."
    start_time = time.time()
    attack_list = nagen.fast_targeted_order(UPA_graph)
    end_time = time.time()
    time_fast_targeted_order.append(end_time - start_time)
    print
    
# Create plot of the result
plt.plot(num_nodes, time_targeted_order, '-b', label='Time targeted_order')
plt.plot(num_nodes, time_fast_targeted_order, '-r', label='Time fast_targeted_order')
plt.legend(loc='upper left')
plt.grid(True)
plt.title("Plot 7: comparison of execution times targeted_order\nand fast_targeted_order ran on a Raspberry Pi (IDLE)")
plt.xlabel("number of nodes in graph")
plt.ylabel("execution time of the function")
plt.show()
