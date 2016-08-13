"""
Code for project #2 of the course Algorithmic Thinking, part 1.
This project is called: Connected Components and Graph Resilience.
"""

# Import statements needed for the functions and classes used
from collections import deque


# Definitions of the functions for this project
def bfs_visited(ugraph, start_node):
    """
    Function that takes the undirected graph ugraph and a start_node in
    this graph and returns a set consisting of all nodes that are visited by
    a breath-first search that starts at start_node.
    """

    # Initialize variables for this function
    _bfs_queue = deque()
    _visited = set([start_node])
    _bfs_queue.append(start_node)

    # Move through the graph using breath-first search
    while len(_bfs_queue) > 0:
        _node = _bfs_queue.popleft()
        for _neighbor in ugraph[_node]:
            if _neighbor not in _visited:
                _visited.add(_neighbor)
                _bfs_queue.append(_neighbor)

    # Return the result of the function
    return _visited


def cc_visited(ugraph):
    """
    Function that takes the undirected graph ugraph and returns a list of sets
    where each set consists of all the nodes (and nothing else) in a connected
    component, and there is exactly one set in the list for each connected
    component in ugraph and nothing else.
    """

    # Initialize variables for this function
    _remaining_nodes = {}
    for _key, _value in ugraph.items():
        _remaining_nodes[_key] = _value
    _cc_set_list = []
    
    # Collect the sets of connected components
    while len(_remaining_nodes) > 0:
        # Select a key in _remaining_nodes
        _keys = _remaining_nodes.keys()
        _start_node = _keys[0]
        # Get a set of connected nodes
        _connected_set = bfs_visited(ugraph, _start_node)
        # Add the set to the resulting list and adapt _remaining_nodes
        _cc_set_list.append(_connected_set)
        _connected_list = list(_connected_set)
        for _node in _connected_list:
            _remaining_nodes.pop(_node)

    # Return the result of the function
    return _cc_set_list


def largest_cc_size(ugraph):
    """
    Function that takes the undirected graph ugraph and returns the size
    (as an integer) of the largest connected component in ugraph.
    """

    # Initialize variables for this function
    _max_size = 0

    # Get a list of sets of connected components
    _cc_set_list = cc_visited(ugraph)

    # Get the size of the largest set of connected components
    for _index in range(len(_cc_set_list)):
        _len_list = len(_cc_set_list[_index])
        if _len_list > _max_size:
            _max_size = _len_list
        
    # Return the result of the function
    return _max_size


def compute_resilience(ugraph, attack_order):
    """
    Function that takes an undirected graph ugraph and a list of nodes
    attack_order and returns a list of the largest connected components
    in the graph after the consequetive removal of the attacked nodes to
    represent the resilience of the network after the attacks. The first
    result in the list is the size of the largest connected component in
    ugraph, the rest of the results in the list is the size of the largest
    connected component after each removal in the order of the list.
    """

    # Initialize variables for this function
    _resilience_list = []
    _resilience_list.append(largest_cc_size(ugraph))
    _counter = 0

    for _attacked_node in attack_order:
        # Remove the attacked node from the network (ugraph)
        _edges_removed_node = ugraph.pop(_attacked_node)
        # Remove all edges pointing to the removed node
        for _edge_removed_node in _edges_removed_node:
            ugraph[_edge_removed_node].remove(_attacked_node)
        # Compute the resilience of the attacked network
        _resilience_list.append(largest_cc_size(ugraph))
        _counter += 1
        if ( _counter % 100 ) == 0:
            print "...............", _counter, "nodes attacked."
    print ".......... All", _counter, "nodes attacked."
            
    # Return the result of the function
    return _resilience_list


"""
# Cases to test the code

EX_GRAPH = {}
EX_GRAPH[0] = set([1,2])
EX_GRAPH[1] = set([0])
EX_GRAPH[2] = set([0])
EX_GRAPH[10] = set([11,13,14,15])
EX_GRAPH[11] = set([10,12,14,16])
EX_GRAPH[12] = set([11,13,15])
EX_GRAPH[13] = set([10,12])
EX_GRAPH[14] = set([10,11])
EX_GRAPH[15] = set([10,12])
EX_GRAPH[16] = set([11])
EX_GRAPH[20] = set([21,24,25,29])
EX_GRAPH[21] = set([20,22,24,26,28])
EX_GRAPH[22] = set([21,23,25,27,28])
EX_GRAPH[23] = set([22,27,29])
EX_GRAPH[24] = set([20,21,29])
EX_GRAPH[25] = set([20,22,29])
EX_GRAPH[26] = set([21,29])
EX_GRAPH[27] = set([22,23,29])
EX_GRAPH[28] = set([21,22])
EX_GRAPH[29] = set([20,23,24,25,26,27])

print "==========> Testing bfs_visited."
print bfs_visited(EX_GRAPH, 0)
print bfs_visited(EX_GRAPH, 1)
print bfs_visited(EX_GRAPH, 2)
print bfs_visited(EX_GRAPH, 10)
print bfs_visited(EX_GRAPH, 20)
print bfs_visited(EX_GRAPH, 29)
print
print "==========> Testing cc_visisted."
print cc_visited(EX_GRAPH)
print
print "==========> Testing largest_cc_size."
print largest_cc_size(EX_GRAPH)
print
print "==========> Testing compute_resilience."
print compute_resilience(EX_GRAPH, [0, 29, 28, 26, 22, 11, 13, 15])
print EX_GRAPH
"""
