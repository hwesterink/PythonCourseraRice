"""
Testing suite for functions developed for project #4:
Computing Alignment of Sequences
"""

import poc_simpletest
import sequence_alignment as sol


##############################################################
# Helper functions to print the results of the tests

def print_scoring_matrix(scoring_matrix, alphabet):
    """
    Helper function that prints out a scoring_matrix
    """

    chars = ""
    for char in alphabet:
        chars += char
    chars += "-"
    print "Scoring matrix for:", chars
    for index in range(len(chars)):
        print "For row", chars[index], "=====>", scoring_matrix[chars[index]]


def print_alignment_matrix(alignment_matrix, seq_x, seq_y):
    """
    Helper function that prints out the alignment_matrix
    """

    row_names = "0" + seq_x
    print "Alignment matrix where columns are: 0" + seq_y
    for index in range(len(seq_x)+1):
        print "For row", row_names[index], "=====>", alignment_matrix[index]
        

##############################################################
# Tests defined for the functions

def run_suite():
    """
    Testing code for the functions written for Sequence Alignment
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()

    ########## First test series - testing "AA" and "TAAT" sequences
    # test build_scoring_matrix
    alphabet = set("ACGT")
    scoring_matrix = sol.build_scoring_matrix(alphabet, 10, 4, -6)
    print_scoring_matrix(scoring_matrix, alphabet)
    print
    
    # test compute global alignment matrix
    print "=====> OUTPUT FIRST TESTS ON 'AA' AND 'TAAT'."
    seq_x = "AA"
    seq_y = "TAAT"
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # test compute_global_alignment
    global_alignment = sol.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print "==================> Global alignment:", global_alignment
    print

    # test to compute local alignment matrix
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # Test compute_local_alignment
    local_alignment = sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print "==================> Local alignment:", local_alignment
    print
    
    ########## Second test series - testing "ACCT" and "TACGGT" sequences
    print "=====> OUTPUT SECOND TESTS ON 'ACCT' AND 'TACGGT'."
    # test to compute global alignment matrix
    seq_x = "ACCT"
    seq_y = "TACGGT"
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # test compute_global_alignment
    global_alignment = sol.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print "==================> Global alignment:", global_alignment
    print
    
    # test for compute_global_alignment using suite.run_test()
    suite.run_test(sol.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix),
                   (22, "-AC-CT", "TACGGT"), "Test #8: testing compute_global_alignment on 'ACCT' and 'TACGGT'.")
    print "==================> Local alignment:", sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print

    ########## Third test series - testing "ACC" and "TTTACACGG" sequences
    print "=====> OUTPUT THIRD TEST ON 'ACC' AND 'TTTACACGG'."
    # test build_scoring_matrix
    scoring_matrix = sol.build_scoring_matrix(alphabet, 10, 2, -4)
    print_scoring_matrix(scoring_matrix, alphabet)
    print
    
    # test to compute global alignment matrix
    seq_x = "ACC"
    seq_y = "TTTACACGG"
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # test compute_global_alignment using suite.run_test()
    suite.run_test(sol.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix),
                   (6, "---AC-C--", "TTTACACGG"), "Test #8: testing compute_global_alignment on 'ACC' and 'TTTACACGG'.")
    print "==================> Global alignment:", sol.compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print

    # test to compute local alignment matrix
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # test compute_local_alignment using suite.run_test()
    suite.run_test(sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix),
                   (26, "AC-C", "ACAC"), "Test #13: testing compute_local_alignment on 'ACC' and 'TTTACACGG'.")
    print "==================> Local alignment:", sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print

    ########## Fouth test series - testing Owltest testcase "ATG" and "ACG" sequences
    print "=====> OUTPUT FOURTH TEST ON 'ATG' AND 'ACG'."
    # test build_scoring_matrix
    scoring_matrix = sol.build_scoring_matrix(alphabet, 6, 2, -4)
    print_scoring_matrix(scoring_matrix, alphabet)
    print
    
    # test to compute local alignment matrix
    seq_x = "ATG"
    seq_y = "ACG"
    alignment_matrix = sol.compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
    print_alignment_matrix(alignment_matrix, seq_x, seq_y)
    print

    # test compute_local_alignment using suite.run_test()
    suite.run_test(sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix),
                   (14, "ATG", "ACG"), "Test #16: testing compute_local_alignment on 'ATG' and 'ACG'.")
    print "==================> Local alignment:", sol.compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
    print

    # report number of tests and failures
    print
    suite.report_results()

run_suite()
