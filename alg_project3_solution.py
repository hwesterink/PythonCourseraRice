"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

######################################################
# Imports needed in the functions

import math
import alg_cluster


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    # Initialize values needed in this function
    _num_clusters = len(cluster_list)
    _result = (float('inf'), -1, -1)

    # Compute all distances between clusters and select the smallest one
    for _index1 in range(_num_clusters):
        for _index2 in range(_num_clusters):
            if _index1 == _index2:
                continue
            _distance = pair_distance(cluster_list, _index1, _index2)
            if _distance[0] < _result[0]:
                _result = _distance
                          
    return _result



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    # Initialize values needed in this function
    _num_clusters = len(cluster_list)

    if _num_clusters <= 3:
        # Base case: only three or less clusters left
        _result = slow_closest_pair(cluster_list)
    else:
        # Recursive devide and conquer case
        _middle = _num_clusters // 2
        _left_clusters = cluster_list[0:_middle]
        _right_clusters = cluster_list[_middle:]
        _left_result = fast_closest_pair(_left_clusters)
        _right_result = fast_closest_pair(_right_clusters)
        # Process the results of the recursions
        _right_result = (_right_result[0], _right_result[1]+_middle, _right_result[2]+_middle)
        if _left_result[0] < _right_result[0]:
            _result = _left_result
        else:
            _result = _right_result
        _line_position = 0.5 * ( cluster_list[_middle-1].horiz_center()
                               + cluster_list[_middle].horiz_center() )
        # Find a possible closest pair around the vertical line separating the clusters
        _strip_result = closest_pair_strip(cluster_list, _line_position, _result[0])
        if _strip_result[0] < _result[0]:
            _result = _strip_result
    
    return _result


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    # Select the clusters in the strip under investigation
    _num_clusters = len(cluster_list)
    _selected_clusters = []
    for _index in range(_num_clusters):
        if abs(cluster_list[_index].horiz_center() - horiz_center) < half_width:
            _current_selection = (cluster_list[_index].vert_center(), _index)
            _selected_clusters.append(_current_selection)

    # Sort the resulting list of indices in nondecreasing order of the vertical
    # coordinates of their associated points
    _selected_clusters.sort()

    # Build a list of the sorted indices
    _len_selection = len(_selected_clusters)
    _cluster_indices = []
    for _index in range(_len_selection):
        _cluster_indices.append(_selected_clusters[_index][1])

    # Initialize values needed in the rest of this function
    _result = (float('inf'), -1, -1)

    # Determine the closest pair in the selected set of clusters    
    for _index1 in range(_len_selection - 1):
        for _index2 in range(_index1+1, min(_index1+4, _len_selection)):
            _distance = (cluster_list[_cluster_indices[_index1]].
                         distance(cluster_list[_cluster_indices[_index2]]))
            if _cluster_indices[_index1] < _cluster_indices[_index2]:
                _new_result = (_distance, _cluster_indices[_index1], _cluster_indices[_index2])
            else:
                _new_result = (_distance, _cluster_indices[_index2], _cluster_indices[_index1])
            if _new_result[0] < _result[0]:
                _result = _new_result

    return _result
            
 
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """

    # Initialize variables and create _new_cluster_list as worklist
    _len_list = len(cluster_list)
    _new_cluster_list = []
    for _index in range(_len_list):
        _copy_cluster = cluster_list[_index].copy()
        _new_cluster_list.append(_copy_cluster)
    # Sort _new_cluster_list by ascending horiz_center for the function fast_closest_pair
    _new_cluster_list.sort(key = lambda cluster: cluster.horiz_center())

    # Merge closest cluster one by one untill the right number of
    # clusters is reached
    while _len_list > num_clusters:
        # Determine closest clusters
        _closest_pair = fast_closest_pair(_new_cluster_list)
        # Join closest clusters, remove the joined cluster and renew _len_list
        ( _new_cluster_list[_closest_pair[1]].
                             merge_clusters(_new_cluster_list[_closest_pair[2]]))
        dummy_joined_cluster = _new_cluster_list.pop(_closest_pair[2])
        _new_cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        _len_list = len(_new_cluster_list)
        if _len_list % 10 == 0:
            print "Now at", _len_list, "clusters."
    
    return _new_cluster_list


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # Initialize variables and create a _work_cluster_list
    _work_cluster_list = []
    for _index1 in range(len(cluster_list)):
        _work_cluster_list.append(cluster_list[_index1].copy())
  
    # Create a _cluster_center_list with intitial output cluster centers and position them
    # at the location of clusters with the largest populations
    _work_cluster_list.sort(key = lambda cluster: cluster.total_population(), reverse = True)
    _cluster_centers = []
    for _index1 in range(num_clusters):
        _cluster_centers.append( (_work_cluster_list[_index1].horiz_center(),
                                  _work_cluster_list[_index1].vert_center()) )

    # Execute iterations
    for _index1 in range(num_iterations):
        # Create a list of empty clusters in _old_cluster_list initialize an empty
        # _output_cluster_list
        _old_cluster_list = []
        _output_cluster_list = []
        for _index2 in range(num_clusters):
            _new_cluster = alg_cluster.Cluster(set([]), _cluster_centers[_index2][0],
                           _cluster_centers[_index2][1], int(0), float(0.0))
            _old_cluster_list.append(_new_cluster)
            _output_cluster_list.append(_new_cluster.copy())
        
        # Merge all clusters from cluster_list to the closest cluster in _work_cluster_list
        for _index2 in range(len(_work_cluster_list)):
            # Find the closest cluster in _old_cluster_list for the selected point
            # from _work_cluster_list
            _min_distance = float('inf')
            _cluster_number = -1
            for _index3 in range(num_clusters):
                _clusters_needed = [ _old_cluster_list[_index3], _work_cluster_list[_index2] ]
                _distance = pair_distance(_clusters_needed, 0, 1)[0]
                if _distance < _min_distance:
                    _min_distance = _distance
                    _cluster_number = _index3
            # Merge this point with the closest cluster in _output_cluster_list
            _output_cluster_list[_cluster_number] = ( _output_cluster_list[_cluster_number].
                            merge_clusters(_work_cluster_list[_index2]) )
        print "Iteration", _index1+1, "completed."

        # Create a new _cluster_centers list with the output cluster centers of the iteration
        for _index2 in range(num_clusters):
            _cluster_centers[_index2] = ( _output_cluster_list[_index2].horiz_center(),
                                          _output_cluster_list[_index2].vert_center() )
            
    return _output_cluster_list
