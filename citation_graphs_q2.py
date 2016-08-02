"""
Code developed for application #1 question 2 of the course
Algorithmic Thinking I
"""

# imports needed for this code
import random
import matplotlib.pyplot as plt
import degree_distributions_v2 as degree

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Helper function for generating the graph

def make_graph_ER(num_nodes, probability):
    """
    Function that creates a directed graph with num_nodes nodes
    represented as an adjacency list using the ER algorithm given in the
    assignment.
    """

    # Create an empty dictionary
    _graph = {}

    # Test num_nodes to determine whether a empty dictionary should be returned
    _num_nodes = int(num_nodes)
    if _num_nodes < 2:
        return _graph

    # Build the graph by adding nodes and edges to the dictionary
    print "====> Creating graph as an adjacency list."
    _counter = 0
    for _index1 in range(0, _num_nodes):
        _edges = list()
        for _index2 in range(0, _num_nodes):
            if _index1 != _index2:
                _select_edge = random.random()
                if _select_edge < probability:
                    _edges.append(_index2)
                    _counter += 1
        _graph[_index1] = set(_edges)
        if _index1 % 100 == 0:
            print "...............", _index1, "nodes processed."
            print "....................", _counter, "edges generated."
    print "...............", _index1, "nodes processed."
    print "....................", _counter, "edges generated."
    print

    # Return the result
    return _graph



#####################################
# Code for answering question 2 of the application

# Create a graph using the ER-algorithm
generated_graph = make_graph_ER(5000, 0.2)

# Compute the in-degree distribution
in_degree_dist = degree.in_degree_distribution(generated_graph)

# Normalize the in-degree distribution and create lists of the data to plot
total = 0
citation_number = []
citation_distr = []
for dummy_key, value in in_degree_dist.items():
    total += value
for key, value in in_degree_dist.items():
    citation_number.append(key)
    citation_distr.append(float(value) / total)

# Create plot of the result
print
print "====> Creating the plot."
plt.loglog(citation_number, citation_distr, 'b.', linestyle='None')
plt.grid(True)
plt.title("Plot 4: loglog plot generated distribution with p=0.2")
plt.xlabel("number of in-degrees (log)")
plt.ylabel("distribution occurrence (log)")
plt.show()
