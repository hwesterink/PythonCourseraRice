"""
Code developed for application #3 question 7 of the course
Algorithmic Thinking II
"""

# imports needed for this code
import urllib2
import alg_cluster
import alg_project3_solution as sol

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
# Code for answering question 7 of the application

# Read the input data for 290 county data and create a list of clusters
data_table = load_data_table(DATA_290_URL)
    
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

# Create the clustered lists needed for computing the distortions
hierarchical_list = sol.hierarchical_clustering(singleton_list, 16)
kmeans_list = sol.kmeans_clustering(singleton_list, 16, 5) 

# Compute and print the distortions
num_clusters = len(kmeans_list)
hierarchical_distortion = 0
kmeans_distortion = 0
for index in range(num_clusters):
    hierarchical_distortion += hierarchical_list[index].cluster_error(data_table)
    kmeans_distortion += kmeans_list[index].cluster_error(data_table)
    
# Print the results
print
print "=====> Results for 290 county datapoints in 16 clusters"
print ".......... Distortion for hiearchical_clustering:", hierarchical_distortion
print ".......... Distortion for kmeans_clustering:     ", kmeans_distortion
print

# Read the input data for 111 county data and create a list of clusters
data_table = load_data_table(DATA_111_URL)
    
singleton_list = []
for line in data_table:
    singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))

# Create the clustered lists needed for computing the distortions
hierarchical_list = sol.hierarchical_clustering(singleton_list, 9)
kmeans_list = sol.kmeans_clustering(singleton_list, 9, 5) 

# Compute and print the distortions
num_clusters = len(kmeans_list)
hierarchical_distortion = 0
kmeans_distortion = 0
for index in range(num_clusters):
    hierarchical_distortion += hierarchical_list[index].cluster_error(data_table)
    kmeans_distortion += kmeans_list[index].cluster_error(data_table)
    
# Print the results
print
print "=====> Results for 111 county datapoints in 16 clusters"
print ".......... Distortion for hiearchical_clustering:", hierarchical_distortion
print ".......... Distortion for kmeans_clustering:     ", kmeans_distortion
