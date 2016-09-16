"""
Testing suite for functions developed for Closest Pairs and Clustering Algorithms
"""

import poc_simpletest
import alg_project3_solution as student
import alg_cluster as CC

def run_suite():
    """
    Testing code for the functions written for Word Wrangler
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()

    # create a set of 3 clusters
    cluster1 = CC.Cluster([1, 1], 0, 0, 100, 0.00001)
    cluster2 = CC.Cluster([2, 2, 2], 3, 4, 200, 0.00002)
    cluster3 = CC.Cluster([3, 3, 3, 3], 6, 8, 300, 0.00003)
    list_of_clusters = [cluster1, cluster2, cluster3]
        
    # testing the slow_closest_pair function with the 3 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (5., 0, 1),
                   "Test #1: testing slow_closest_pair on 3 clusters")
    # testing the fast_closest_pair function with the 3 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (5., 0, 1),
                   "Test #2: testing fast_closest_pair on 3 clusters")

    # add a fourth cluster to the list
    cluster4 = CC.Cluster([4, 4, 4, 4, 4], 12, 16, 400, 0.00004)
    list_of_clusters.append(cluster4)

    # testing the slow_closest_pair function with the 4 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (5., 0, 1),
                   "Test #3: testing slow_closest_pair on 4 clusters")
    # testing the fast_closest_pair function with the 4 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (5., 0, 1),
                   "Test #4: testing fast_closest_pair on 4 clusters")

    # create a set of 4 clusters
    cluster1 = CC.Cluster(set([]), 0, 0, 1, 0)
    cluster2 = CC.Cluster(set([]), 1, 0, 1, 0)
    cluster3 = CC.Cluster(set([]), 2, 0, 1, 0)
    cluster4 = CC.Cluster(set([]), 3, 0, 1, 0)
    list_of_clusters = [cluster1, cluster2, cluster3, cluster4]
        
    # testing closest_pair_strip on 4 clusters
    suite.run_test(student.closest_pair_strip(list_of_clusters, 1.5, 1.0), (1.0, 1, 2),
                   "Test #5: testing closest_pair_strip on 4 clusters")

    # create a set of 4 clusters
    cluster1 = CC.Cluster(set([]), 1.0, 0.0, 1, 0)
    cluster2 = CC.Cluster(set([]), 4.0, 0.0, 1, 0)
    cluster3 = CC.Cluster(set([]), 5.0, 0.0, 1, 0)
    cluster4 = CC.Cluster(set([]), 7.0, 0.0, 1, 0)
    list_of_clusters = [cluster1, cluster2, cluster3, cluster4]
        
    # testing fast_closest_pair on 4 clusters
    suite.run_test(student.fast_closest_pair(list_of_clusters), (1.0, 1, 2),
                   "Test #6: testing closest_pair_strip on 4 clusters")

    # create a set of 4 clusters
    cluster1 = CC.Cluster(set([]), -4.0, 0.0, 1, 0)
    cluster2 = CC.Cluster(set([]), 0.0, -1.0, 1, 0)
    cluster3 = CC.Cluster(set([]), 0.0, 1.0, 1, 0)
    cluster4 = CC.Cluster(set([]), 4.0, 0.0, 1, 0)
    list_of_clusters = [cluster1, cluster2, cluster3, cluster4]
        
    # testing closest_pair_strip on 4 clusters
    suite.run_test(student.closest_pair_strip(list_of_clusters, 0.0, 4.1231059999999999), (2.0, 1, 2),
                   "Test #7: testing closest_pair_strip on 4 clusters")

    # create a set of 4 clusters
    cluster1 = CC.Cluster(set([]), -4.0, 0.0, 1, 0)
    cluster2 = CC.Cluster(set([]), 0.0, -1.0, 1, 0)
    cluster3 = CC.Cluster(set([]), 0.0, 1.0, 1, 0)
    cluster4 = CC.Cluster(set([]), 4.0, 0.0, 1, 0)
    list_of_clusters = [cluster1, cluster2, cluster3, cluster4]
        
    # testing fast_closest_pair on 4 clusters
    suite.run_test(student.fast_closest_pair(list_of_clusters), (2.0, 1, 2),
                   "Test #8: testing fast_closest_pair on 4 clusters")

    # create a sorted list_of_clusters from a small dataset containing 8 clusters
    fhandle = open("unifiedCancerData_8.txt")
    list_of_clusters = []
    for line in fhandle:
        tokens = line.split(',')
        cluster = CC.Cluster(set([tokens[0]]), float(tokens[1]), float(tokens[2]),
                             int(tokens[3]), float(tokens[4]))
        list_of_clusters.append(cluster)
    list_of_clusters.sort(key = lambda cluster: cluster.horiz_center())
    print "The following list_of_clusters was loaded:"
    for index in range(len(list_of_clusters)):
        print index, list_of_clusters[index]
    print

    # testing the slow_closest_pair function with 8 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (2.4479655653349655, 5, 7),
                   "Test #9: testing slow_closest_pair on 8 clusters")
    # testing the fast_closest_pair function with 8 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (2.4479655653349655, 5, 7),
                   "Test #10: testing fast_closest_pair on 8 clusters")
    # testing the hierarchical_clustering function with 8 clusters
    clustering_result = student.hierarchical_clustering(list_of_clusters, 5)
    for index in range(len(clustering_result)):
        print clustering_result[index]
    print
    # testing the kmeans_clustering function with 8 clusters
    clustering_result = student.kmeans_clustering(list_of_clusters, 5, 3)
    for index in range(len(clustering_result)):
        print clustering_result[index]
    print

    # create a sorted list_of_clusters from a small dataset containing 17 clusters
    fhandle = open("unifiedCancerData_17.txt")
    list_of_clusters = []
    for line in fhandle:
        tokens = line.split(',')
        cluster = CC.Cluster(set([tokens[0]]), float(tokens[1]), float(tokens[2]),
                             int(tokens[3]), float(tokens[4]))
        list_of_clusters.append(cluster)
    list_of_clusters.sort(key = lambda cluster: cluster.horiz_center())
 
    # testing the slow_closest_pair function with 17 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (1.9439662413427632, 9, 10),
                   "Test #11: testing slow_closest_pair on 17 clusters")
    # testing the fast_closest_pair function with 17 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (1.9439662413427632, 9, 10),
                   "Test #12: testing fast_closest_pair on 17 clusters")

    # create a sorted list_of_clusters from a small dataset containing 24 clusters
    fhandle = open("unifiedCancerData_24.txt")
    list_of_clusters = []
    for line in fhandle:
        tokens = line.split(',')
        cluster = CC.Cluster(set([tokens[0]]), float(tokens[1]), float(tokens[2]),
                             int(tokens[3]), float(tokens[4]))
        list_of_clusters.append(cluster)
    list_of_clusters.sort(key = lambda cluster: cluster.horiz_center())
    print "The following list_of_clusters was loaded:"
    for index in range(len(list_of_clusters)):
        print index, list_of_clusters[index]
    print

    # testing the kmeans_clustering function with 24 clusters
    clustering_result = student.kmeans_clustering(list_of_clusters, 10, 1)
    print "This output was created by kmeans_slustering:"
    for index in range(len(clustering_result)):
        print index, clustering_result[index]
    print

    # create a sorted list_of_clusters from a small dataset containing 39 clusters
    fhandle = open("unifiedCancerData_39.txt")
    list_of_clusters = []
    for line in fhandle:
        tokens = line.split(',')
        cluster = CC.Cluster(set([tokens[0]]), float(tokens[1]), float(tokens[2]),
                             int(tokens[3]), float(tokens[4]))
        list_of_clusters.append(cluster)
    list_of_clusters.sort(key = lambda cluster: cluster.horiz_center())
 
    # testing the slow_closest_pair function with 39 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (1.6612217536988727, 22, 24),
                   "Test #13: testing slow_closest_pair on 39 clusters")
    # testing the fast_closest_pair function with 39 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (1.6612217536988727, 22, 24),
                   "Test #14: testing fast_closest_pair on 39 clusters")

    # create a sorted list_of_clusters from a small dataset containing 111 clusters
    fhandle = open("unifiedCancerData_111.csv")
    list_of_clusters = []
    for line in fhandle:
        tokens = line.split(',')
        cluster = CC.Cluster(set([tokens[0]]), float(tokens[1]), float(tokens[2]),
                             int(tokens[3]), float(tokens[4]))
        list_of_clusters.append(cluster)
    list_of_clusters.sort(key = lambda cluster: cluster.horiz_center())
    print "The following list_of_clusters was loaded:"
    for index in range(len(list_of_clusters)):
        print index, list_of_clusters[index]
    print
 
    # testing the slow_closest_pair function with 111 cluster list
    suite.run_test(student.slow_closest_pair(list_of_clusters), (1.266216002018164, 79, 81),
                   "Test #15: testing slow_closest_pair on 111 clusters")
    # testing the fast_closest_pair function with 111 cluster list    
    suite.run_test(student.fast_closest_pair(list_of_clusters), (1.266216002018164, 79, 81),
                   "Test #16: testing fast_closest_pair on 111 clusters")
    # testing the hierarchical_clustering function with 111 clusters
    clustering_result = student.hierarchical_clustering(list_of_clusters, 5)
    for index in range(len(clustering_result)):
        print clustering_result[index]
    print

    # report number of tests and failures
    print
    suite.report_results()

run_suite()
