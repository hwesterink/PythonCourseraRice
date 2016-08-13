"""
General code developed for application #2 of the course Algorithmic Thinking I.
This code loads or generates the graphs used to answer the questions of
application #2.
"""

# imports needed for this code
import urllib2
import random
import UPATrail_class as UPA
import degree_distributions_v2 as degree

# CodeSkulptor imports (only if this code is run in Code Skulptor)
#import simpleplot
#import codeskulptor
#codeskulptor.set_timeout(20)


############################################
# Provided code as helper functions for the application

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # copy the graph
    new_graph = copy_graph(ugraph)
    
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        neighbors = new_graph[max_degree_node]
        new_graph.pop(max_degree_node)
        for neighbor in neighbors:
            new_graph[neighbor].remove(max_degree_node)
        order.append(max_degree_node)

    return order
    

###################################
# Function for loading the graph representing the Computer Network

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
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


###################################
# Function for generating an undirected ER graph

def make_graph_ER(num_nodes, probability):
    """
    Function that creates an undirected graph with num_nodes nodes
    represented as an adjacency list using an adapted ER algorithm given in
    assignment #1: 'Analysis of Citation Graphs' to generate the edges.
    """

    # Create an empty dictionary
    _graph = {}

    # Test num_nodes to determine whether a empty dictionary should be returned
    _num_nodes = int(num_nodes)
    if _num_nodes < 2:
        return _graph

    # Build the graph by adding nodes and edges to the dictionary
    print "====> Creating ER graph as an adjacency list."
    # Create a graph without edges
    for _index in range(_num_nodes):
        _graph[_index] = set()
    print "...............", _num_nodes, "nodes generated."
    # Generate edges based on the given probability
    _counter = 0
    for _index1 in range(_num_nodes):
        for _index2 in range(_index1+1, _num_nodes):
            _select_edge = random.random()
            if _select_edge < probability:
                _graph[_index1].add(_index2)
                _graph[_index2].add(_index1)
                _counter += 1
        if _counter % 100 == 0:
            print "....................", _counter, "edges generated."
    print "....................", _counter, "edges generated."

    # Return the result
    return _graph


###################################
# Function for generating an undirected UPA graph

def make_graph_UPA(num_nodes, num_edges_per_node):
    """
    Function that creates an undirected graph with num_nodes nodes
    represented as an adjacency list using an adapted DPA algorithm given in
    assignment #1: 'Analysis of Citation Graphs' to generate the edges.
    """
    
    # Test num_nodes and num_edges_per_node to determine whether
    # the algoritnm can be used
    _num_nodes = int(num_nodes)
    _num_edges_per_node = int(num_edges_per_node)
    if _num_nodes < _num_edges_per_node:
        print "###> Error: _num_nodes must be larger than or equal to _num_edges_per_node!"
        quit()

    # Create a complete graph of size num_edges_per_node
    print "Generating the initial graph."
    _graph = degree.make_complete_graph(_num_edges_per_node)

    # Initialize variables
    _node_counter = _num_edges_per_node
    _edge_counter = int( 0.5 * _num_edges_per_node * ( _num_edges_per_node - 1 ))
    print "...............", _node_counter, "nodes generated."
    print "....................", _edge_counter, "edges generated."
    print

    # Add nodes to graph according to the UPA algorithm
    # Create UPATrial object that is used to generate the edges with
    # the newly generated nodes
    _trail = UPA.UPATrial(_num_edges_per_node)
    print "Generating additional nodes."
    for _index in range(_num_edges_per_node, _num_nodes):
        # Create additional node
        _new_nodes_edges = _trail.run_trial(_num_edges_per_node)
        # Add the new node to _graph
        _graph[_index] = _new_nodes_edges
        # Add the edges from the selected nodes to the new node
        for _node in _new_nodes_edges:
            _graph[_node].add(_index)
        _node_counter += 1
        _edge_counter += len(_new_nodes_edges)
        if _node_counter % 100 == 0:
            print "...............", _node_counter, "nodes generated."
    print "...............", _node_counter, "nodes generated."
    print "....................", _edge_counter, "edges generated."

    # Return the resulting graph
    return _graph


###################################
# Function to compute a targeted attack order consisting of nodes of
# maximal degree

def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes
    """
    # Create a copy of the graph to work in
    _work_graph = copy_graph(ugraph)
    
    # Initialize empty sets for the degrees of the nodes
    _num_nodes = len(_work_graph)
    _degree_sets = {}
    for _index in range(_num_nodes):
        _degree_sets[_index] = set()

    # Fill the degree_sets with the nodes of the right degrees
    for _node, _edges in _work_graph.items():
        _node_degree = len(_edges)
        _degree_sets[_node_degree].add(_node)

    # Initialize additional variables
    _attack_order = []
    _removed_nodes = 0

    # Create a list of nodes to remove starting with the nodes with the
    # highest degrees
    for _index in range(_num_nodes - 1, -1, -1):
        while len(_degree_sets[_index]) > 0:
            # Select an arbitrairy node and remove it from the selected
            # degree_set
            _node_selected = _degree_sets[_index].pop()
            # Remove all edges to the selected node and adapt the
            # degree_sets accordingly
            for _neighbor_node in _work_graph[_node_selected]:
                _degree_neighbor = len(_work_graph[_neighbor_node])
                _degree_sets[_degree_neighbor].remove(_neighbor_node)
                _degree_sets[_degree_neighbor - 1].add(_neighbor_node)
            # Add the removed node to the _attack_order
            _attack_order.append(_node_selected)
            _removed_nodes += 1
            # Remove the selected node and its edges from the graph
            delete_node(_work_graph, _node_selected)

    # Return the attack_order
    return _attack_order
    

"""
#################################
# Code to test the functions above

print "==========> Testing load_graph."
ugraph = load_graph(NETWORK_URL)
for index in range(10):
    print ugraph[index]

print
print "==========> Testing make_graph_ER."
ugraph = make_graph_ER(1239, 0.0040)
for index in range(10):
    print ugraph[index]

print
print "==========> Testing make_graph_UPA."
ugraph = make_graph_UPA(1239, 2)
for index in range(1229,1239):
    print ugraph[index]
"""
