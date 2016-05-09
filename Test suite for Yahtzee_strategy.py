"""
Testing suite for Yahtzee strategy planner
"""

import PoC_simpletest_module as poc_simpletest
import Yahtzee_strategy_v2 as yahtzee_functions

def prt_sorted_set(input_set, items_p_line=5):
    """
    Function that prints a set of tuples in a controlled and sorted manner
    """
    output_list = list(input_set)
    output_list.sort()
    for idx1 in range(len(output_list) / items_p_line):
        output = ""
        for idx2 in range(items_p_line):
            output += str(output_list[items_p_line*idx1 + idx2]) + "; "
        if ((len(output_list)%items_p_line == 0) and
            (idx1 == len(output_list) / items_p_line - 1)):
            output = output[0: -2]
        print output
    output = ""
    for idx in range(len(output_list)-len(output_list)%items_p_line, len(output_list)):
        output += str(output_list[idx]) + "; "
    if len(output) != 0:
        output = output[0: -2] + "\n"
        print output
    else:
        print

def run_suite1():
    """
    Tests for the Yahtzee strategy planner during development of the
    mini-project Yahtzee (PoC 1 Week 4)
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # Testing code for the functions gen_all_holds and score
    hand = tuple([])
    suite.run_test(yahtzee_functions.score(hand), 0, "Test #1:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([()]), "Test #2:")

    hand = tuple([5])
    suite.run_test(yahtzee_functions.score(hand), 5, "Test #3:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (5,)]), "Test #4:")

    hand = tuple([2, 4])
    suite.run_test(yahtzee_functions.score(hand), 4, "Test #5:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (2,), (4,), (2, 4)]), "Test #6:")
    
    hand = tuple((3, 3, 3))
    suite.run_test(yahtzee_functions.score(hand), 9, "Test #7:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (3,), (3, 3), (3, 3, 3)]), "Test #8:")

    hand = tuple((1, 2, 2))
    suite.run_test(yahtzee_functions.score(hand), 4, "Test #9:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)]), "Test #10:")

    hand = tuple([2, 3, 6])
    suite.run_test(yahtzee_functions.score(hand), 6, "Test #11:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)]), "Test #12:")

    hand = tuple([1, 2, 3, 6])
    suite.run_test(yahtzee_functions.score(hand), 6, "Test #13:")
    suite.run_test(yahtzee_functions.gen_all_holds(hand),
                   set([(), (1,), (2,), (3,), (6,),
                        (1, 2), (1, 3), (1, 6), (2, 3), (2, 6), (3, 6),
                        (1, 2, 3), (1, 2, 6), (1, 3, 6), (2, 3, 6), (1, 2, 3, 6)]), "Test #14:")

    hand = tuple([1, 2, 3, 5, 6])
    suite.run_test(yahtzee_functions.score(hand), 6, "Test #15:")
    holds = yahtzee_functions.gen_all_holds(hand)
    prt_sorted_set(holds)

    hand = tuple([1, 4, 4, 6, 6])
    suite.run_test(yahtzee_functions.score(hand), 12, "Test #16:")
    holds = yahtzee_functions.gen_all_holds(hand)
    prt_sorted_set(holds)
    
    hand = tuple([4, 4, 6, 6, 6])
    suite.run_test(yahtzee_functions.score(hand), 18, "Test #17:")
    holds = yahtzee_functions.gen_all_holds(hand)
    prt_sorted_set(holds, 4)
    
    hand = tuple([5, 5, 5, 5, 5])
    suite.run_test(yahtzee_functions.score(hand), 25, "Test #18:")
    holds = yahtzee_functions.gen_all_holds(hand)
    prt_sorted_set(holds)
    
    hand = tuple([2, 3, 4, 5, 5, 6])
    suite.run_test(yahtzee_functions.score(hand), 10, "Test #19:")
    holds = yahtzee_functions.gen_all_holds(hand)
    prt_sorted_set(holds)

    # Testing the function expected_value

    hold = tuple()
    suite.run_test(yahtzee_functions.expected_value(hold, 6, 1), 3.5, "Test #20:")

    hold = tuple([6, 6])
    suite.run_test(yahtzee_functions.expected_value(hold, 6, 1), 13.0, "Test #21:")

    hold = tuple([5, 5])
    suite.run_test(yahtzee_functions.expected_value(hold, 5, 1), 11.0, "Test #22:")
    
    
    # report number of tests and failures
    suite.report_results()

    
    
run_suite1()
