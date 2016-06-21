"""
Testing suite for functions developed for Word Wrangler
"""

import poc_simpletest
import user41_BcfG4WVs1z_21 as wrangler

def run_suite():
    """
    Testing code for the functions written for Word Wrangler
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()
    
    # testing the remove_duplicates function
    input_list = ["", "a", "a", "aa", "aa", "aab", "aab", "ab", "ab", "aba", "aba", 
                  "b", "ba", "ba", "baa", "baa"]
    suite.run_test(wrangler.remove_duplicates(input_list), ["", "a", "aa", "aab", "ab",
                  "aba", "b", "ba", "baa"], "Test #1: testing remove_duplicates")
    
    # testing the intersect function
    list1 = ["", "a", "a", "aa", "aa", "aab", "aab", "ab", "ab", "aba", "aba", 
             "b", "ba", "ba", "baa", "baa"]
    list2 = ["", "a", "a", "aa", "aa", "aab", "aab", "ab", "ab", "aba", "aba", 
             "b", "ba", "ba", "baa", "baa"]
    suite.run_test(wrangler.intersect(list1, list2), ["", "a", "a", "aa", "aa",
             "aab", "aab", "ab", "ab", "aba", "aba", "b", "ba", "ba", "baa", "baa"], 
             "Test #2: testing intersect")
    list1 = ["", "a", "aa", "aab", "ab", "aba", "b", "ba", "baa"]
    suite.run_test(wrangler.intersect(list1, list2), ["", "a", "aa", "aab", "ab",
             "aba", "b", "ba", "baa"], "Test #3: testing intersect")
    list1 = ["", "a", "aa", "aab", "ab", "aba", "b", "ba", "baa"]
    list2 = ["a", "a", "aa", "aa", "aba", "aba", "b", "ba", "ba"]
    suite.run_test(wrangler.intersect(list1, list2), ["a", "aa", "aba", "b", "ba"],
             "Test #4: testing intersect")

    # testing the merge function
    list1 = ["", "a", "aa", "aab", "ab", "aba", "b", "ba", "baa"]
    list2 = ["a", "aa", "aab", "ab", "aba", "ba", "baa"]
    suite.run_test(wrangler.merge(list1, list2), ["", "a", "a", "aa", "aa",
             "aab", "aab", "ab", "ab", "aba", "aba", "b", "ba", "ba", "baa", "baa"], 
             "Test #5: testing merge")
    
    # testing the merge_sort function
    list1 = ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab",
             "aba", "aba", "baa", "baa"]
    suite.run_test(wrangler.merge_sort(list1), ["", "a", "a", "aa", "aa",
             "aab", "aab", "ab", "ab", "aba", "aba", "b", "ba", "ba", "baa", "baa"], 
             "Test #6: testing merge_sort")
    
    # testing the gen_all_strings function
    word = "aab"
    suite.run_test(wrangler.gen_all_strings(word), ["", "b", "a", "ab", "ba", "a",
             "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"], 
             "Test #7: gen_all_strings")
    
    # testing the load_words function

    # example of a run_test call for poc_simpletest
    #suite.run_test(wrangler.remove_duplicates(word_list), ["a", "b", "ab", "ba"],
    #                                          "Test #1: testing remove_duplicates")
    
    # report number of tests and failures
    print
    suite.report_results()

run_suite()
