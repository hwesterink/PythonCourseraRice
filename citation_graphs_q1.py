"""
Code developed for application #1 question 1 of the course
Algorithmic Thinking I
"""

# imports needed for this code
import urllib2
import matplotlib.pyplot as plt
import degree_distributions_v2 as degree

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Helper function for loading the citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph as an adjacency list
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


#####################################
# Code to load the graph and test it was loaded correctly

# Load the graph
citation_graph = load_graph(CITATION_URL)

counter = 1
for key, value in citation_graph.items():
    print counter, key, value
    counter += 1
    if counter > 10:
        break

print


#####################################
# Code for answering question 1 of the application

# Compute the in-degree distribution
in_degree_dist = degree.in_degree_distribution(citation_graph)

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
plt.loglog(citation_number, citation_distr, 'b.', linestyle='None')
plt.grid(True)
plt.title("Plot 1: loglog plot citation distribution")
plt.xlabel("number of citations (log)")
plt.ylabel("distribution occurrence (log)")
plt.show()
