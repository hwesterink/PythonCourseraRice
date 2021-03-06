"""
Code developed for application #2 question 1 of the course
Algorithmic Thinking I
"""

# Imports needed for this code
import random
import connections_analysis as ca
import network_analysis_gen as nagen
import matplotlib.pyplot as plt

# CodeSkulptor imports (only if this code is run in Code Skulptor)
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Helper function to generate a random order to attack the networks

def random_order(ugraph):
    """
    Function that takes an undirected graph and generates an random attack
    order to attack the network represented by the graph
    """
    _attack_order = ugraph.keys()
    random.shuffle(_attack_order)

    return _attack_order


#####################################
# Code for answering question 1 of the application

# Load the network-graph
print "==========> Loading the network-graph"
network_graph = nagen.load_graph(nagen.NETWORK_URL)
# Generate the ER-graph
print
print "==========> Generating the ER-graph"
er_graph = nagen.make_graph_ER(1239, 0.0040)
# Generate the UPA-graph
print
print "==========> Generating the UPA-graph"
upa_graph = nagen.make_graph_UPA(1239, 3)

# Generate the attack orders for the three networks
print
print "==========> Generating attack schedules"
network_attack = random_order(network_graph)
er_attack = random_order(er_graph)
upa_attack = random_order(upa_graph)

# Attack the computer-network
print
print "==========> Attacking the computer-network"
network_resilience = ca.compute_resilience(network_graph, network_attack)
# Attack the ER-network
print
print "==========> Attacking the ER-network"
er_resilience = ca.compute_resilience(er_graph, er_attack)
# Attack the UPA-network
print
print "==========> Attacking the UPA-network"
upa_resilience = ca.compute_resilience(upa_graph, upa_attack)

# Create a list for the x-axis
x_axis = range(1240)

# Create plot of the result
plt.plot(x_axis, network_resilience, '-b', label='Computer network')
plt.plot(x_axis, er_resilience, '-r', label='ER-graph with p=0.0040')
plt.plot(x_axis, upa_resilience, '-g', label='UPA-graph with m=3')
plt.legend(loc='upper right')
plt.grid(True)
plt.title("Plot 6: comparison of graph resilience for random attack order")
plt.xlabel("number of nodes removed")
plt.ylabel("largest set of connected components")
plt.show()
