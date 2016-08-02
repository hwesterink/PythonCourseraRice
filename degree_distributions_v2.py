"""
Code for project #1 of the course Algorithmic Thinking, part 1.
This project is called: Degree Distributions for Graphs.
"""

# The constants containing the graphs used for this project

EX_GRAPH0 = {}
EX_GRAPH0[0] = set([1,2])
EX_GRAPH0[1] = set([])
EX_GRAPH0[2] = set([])
EX_GRAPH1 = {}
EX_GRAPH1[0] = set([1,4,5])
EX_GRAPH1[1] = set([2,6])
EX_GRAPH1[2] = set([3])
EX_GRAPH1[3] = set([0])
EX_GRAPH1[4] = set([1])
EX_GRAPH1[5] = set([2])
EX_GRAPH1[6] = set([])
EX_GRAPH2 = {}
EX_GRAPH2[0] = set([1,4,5])
EX_GRAPH2[1] = set([2,6])
EX_GRAPH2[2] = set([3,7])
EX_GRAPH2[3] = set([7])
EX_GRAPH2[4] = set([1])
EX_GRAPH2[5] = set([2])
EX_GRAPH2[6] = set([])
EX_GRAPH2[7] = set([3])
EX_GRAPH2[8] = set([1,2])
EX_GRAPH2[9] = set([0,3,4,5,6,7])


# Definitions of the functions for this project

def make_complete_graph(num_nodes):
    """
    Function that creates a directed complete graph with num_nodes nodes
    represented as an adjacency list.
    Complete means that all possible edges are created with the ecxeption of
    self-loops.
    """

    # Create an empty dictionary
    _graph = {}

    # Test num_nodes to determine whether a empty dictionary should be returned
    _num_nodes = int(num_nodes)
    if _num_nodes < 2:
        return _graph

    # Build the graph by adding nodes and edges to the dictionary
    for _index1 in range(0, _num_nodes):
        _edges = list()
        for _index2 in range(0, _num_nodes):
            if _index1 != _index2:
                _edges.append(_index2)
        _graph[_index1] = set(_edges)

    # Return the result
    return _graph

def compute_in_degrees(digraph):
    """
    Function that returns a dictionary of the in-degrees of all nodes of the
    directed input graph digraph, that must be represented as an adjacency list.
    """

    # Create an empty result dictionary
    _in_degrees = {}

    # Determine the in-degrees of each node
    _counter = 0
    print "====> Processing graph into in-degree matrix."
    for dummy_key, _values in digraph.items():
        for _value in _values:
            _in_degrees[_value] = _in_degrees.get(_value, 0) + 1
        _counter += 1
        if _counter % 1000 == 0:
            print "...............", _counter, "nodes processed."
    for _key in digraph:
        _in_degrees[_key] = _in_degrees.get(_key, 0)
        
    # Return the result
    return _in_degrees

def in_degree_distribution(digraph):
    """
    Function that returns a dictionary with the in-degree distribution.
    In this dictionary the key is the in-degree, the value is the number
    of times it occurs in the input directed graph digraph.
    """

    # Create and empty result dictionary
    _in_degree_dist = {}

    # Create the distionary of in-degrees of digraph
    _in_degrees = compute_in_degrees(digraph)

    # Build the in-degree distibution dictionary
    _counter = 0
    print
    print "====> Processing graph into in-degree distribution."
    for _key, _value in _in_degrees.items():
        _in_degree_dist[_value] = _in_degree_dist.get(_value, 0) + 1
        _counter += 1
        if _counter % 10000 == 0:
            print "...............", _counter, "nodes processed."

    # Return the result
    return _in_degree_dist
    

"""
# Code to call and test the functions
print EX_GRAPH0
print EX_GRAPH1
print EX_GRAPH2

# Testing make_complete graph
print make_complete_graph(4)
print make_complete_graph(1)
print make_complete_graph(3.5)

# Testing compute_in_degrees
print "===> IN_DEGREES"
print compute_in_degrees(EX_GRAPH0)
print compute_in_degrees(EX_GRAPH1)
print compute_in_degrees(EX_GRAPH2)
print compute_in_degrees(make_complete_graph(5))
print

# Testing in_degree_distribution
print "===> IN_DEGREE_DISTRIBUTIONS"
print in_degree_distribution(EX_GRAPH0)
print in_degree_distribution(EX_GRAPH1)
print in_degree_distribution(EX_GRAPH2)
print in_degree_distribution(make_complete_graph(5))
"""
