"""
Code developed for application #1 question 4 of the course
Algorithmic Thinking I
"""

# imports needed for this code
import DPATrial_class as DPA
import matplotlib.pyplot as plt
import degree_distributions_v2 as degree

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################
# Helper function for generating the graph

def make_graph_DPA(num_nodes, num_edges_per_node):
    """
    Function that creates a directed graph with num_nodes nodes
    represented as an adjacency list using the DPA algorithm given in the
    assignment.
    """
    
    # Test num_nodes and num_edges_per_node to determine whether
    # the algoritnm can be used
    _num_nodes = int(num_nodes)
    _num_edges_per_node = int(num_edges_per_node)
    if _num_nodes < _num_edges_per_node:
        print "###> Error: _num_nodes must be larger than or eagle to _num_edges_per_node!"
        quit()

    # Create a complete graph of size num_edges_per_node and compute its in degrees
    print "Generating the initial graph."
    _graph = degree.make_complete_graph(_num_edges_per_node)

    # Initialize variables
    _counter = _num_edges_per_node

    # Add nodes to graph according to the DPA algorithm
    # Create DPATrial object the is used to generate the edges with the new nodes
    _trail = DPA.DPATrial(_num_edges_per_node)
    print "Generating additional nodes."
    for _index in range(_num_edges_per_node, _num_nodes):
        # Create additional node
        _new_nodes_edges = _trail.run_trial(_num_edges_per_node)
        # Add the new node to _graph
        _graph[_index] = _new_nodes_edges
        _counter += 1
        if _counter % 1000 == 0:
            print "...............", _counter, "nodes generated."

    # Return the resulting graph
    return _graph


#####################################
# Code for answering question 4 of the application

# Create a graph using the DPA-algorithm
generated_graph = make_graph_DPA(27700, 13)

# Compute and print the edges generated
tot_edges = 0
for key, value in generated_graph.items():
    tot_edges += len(value)
print
print "Total number of edges created =", tot_edges
print

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
plt.title("Plot 5: loglog plot DPA generated distribution")
plt.xlabel("number of in-degrees (log)")
plt.ylabel("distribution occurrence (log)")
plt.show()
