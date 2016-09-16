"""
Code developed for application #3 question 10 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import urllib2
import alg_cluster
import alg_project3_solution as sol
import matplotlib.pyplot as plt

# Set timeout for CodeSkulptor (only if this code is run in Code Skulptor)
#import codeskulptor
#codeskulptor.set_timeout(20)


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


#####################################
# Code for answering question 10 of the application for 111 county datapoints

# Read the input data for 896 county data and create a list of clusters
data_table = load_data_table(DATA_896_URL)
    
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

# Create a list for the x-axis and initialize additional lists for the outcomes
x_axis = range(6, 21)
hierarchical_distortions = []
kmeans_distortions = []
for index in range(15):
    hierarchical_distortions.append(0)
    kmeans_distortions.append(0)

# Compute the lists of distortions for the graph
## - Compute the list for the hierarchical_clustering algorithm
##   (start with 20 clusters)
hierarchical_list = sol.hierarchical_clustering(singleton_list, 20)
for index in range(20):
    hierarchical_distortions[14] += hierarchical_list[index].cluster_error(data_table)
##   (now create the datapoints 19 through 6)
for index1 in range(19, 5, -1):
    hierarchical_list = sol.hierarchical_clustering(hierarchical_list, index1)
    for index2 in range(index1):
        hierarchical_distortions[index1 - 6] += hierarchical_list[index2].cluster_error(data_table)

## - Compute the list for the kmeans_clustering algorithm
##   (create the datapoints 6 through 20)
for index1 in range(6, 21):
    kmeans_list = sol.kmeans_clustering(singleton_list, index1, 5)
    for index2 in range(index1):
        kmeans_distortions[index1 - 6] += kmeans_list[index2].cluster_error(data_table)
    print "..... Distortion computed for", index1, "clusters."
    
# Create plot of the result
plt.plot(x_axis, hierarchical_distortions, '-b', label='hierarchical-clustering')
plt.plot(x_axis, kmeans_distortions, '-r', label='kmeans-clustering')
plt.legend(loc='upper right')
plt.grid(True)
plt.title("Plot 16: distortions hierarchical- and kmeans-clustering\nfor 896 datapoints")
plt.xlabel("number of clusters")
plt.ylabel("distortion")
plt.show()
