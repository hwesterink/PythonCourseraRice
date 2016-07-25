"""
Testing suite for methods developed for Fifteen Puzzle solver
"""

import poc_simpletest
import user41_rJZfIie72I_75 as solver

def run_suite():
    """
    Testing code for the methods written for the Fifteen Puzzle solver
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()
    
    # create scrumbled boards to test the solver methods with
    init_board = [[4, 2, 8, 7], [3, 5, 6, 10], [9, 1, 0, 11], [12, 13, 14, 15]]
    PuzzleBoard0 = solver.Puzzle(4, 4, init_board)
    init_board = [[8, 1, 2, 3], [9, 6, 4, 7], [5, 0, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard1 = solver.Puzzle(4, 4, init_board)
    init_board = [[1, 2, 6, 3], [4, 5, 11, 10], [8, 0, 9, 6], [12, 13, 14, 15]]
    PuzzleBoard2 = solver.Puzzle(4, 4, init_board)
    init_board = [[4, 1, 9, 2], [8, 6, 7, 3], [5, 0, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard3 = solver.Puzzle(4, 4, init_board)
    init_board = [[10, 4, 6, 5], [1, 8, 3, 7], [11, 9, 2, 0], [12, 13, 14, 15]]
    PuzzleBoard4 = solver.Puzzle(4, 4, init_board)
    init_board = [[8, 7, 1], [5, 4, 3], [2, 6, 0]]
    PuzzleBoard5 = solver.Puzzle(3, 3, init_board)
    init_board = [[2, 8, 6, 5], [1, 4, 3, 7], [0, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard6 = solver.Puzzle(4, 4, init_board)
    print PuzzleBoard0
    print
    print PuzzleBoard1
    print
    print PuzzleBoard3
    print
    print PuzzleBoard4
    print
    print PuzzleBoard5
    print
    
    # testing the lower_row_invariant method
    suite.run_test(PuzzleBoard1.lower_row_invariant(2, 1), True,
                   "Test #1: first test for lower_row_invariant method")
    suite.run_test(PuzzleBoard2.lower_row_invariant(2, 1), False,
                   "Test #2: second test for lower_row_invariant method")
    suite.run_test(PuzzleBoard3.lower_row_invariant(2, 1), True,
                   "Test #3: third test for lower_row_invariant method")
    suite.run_test(PuzzleBoard4.lower_row_invariant(2, 3), True,
                   "Test #4: fourth test for lower_row_invariant method")
    
    # testing the solve_interior_tile method
    print "###solve_interior_tile###"
    suite.run_test(PuzzleBoard0.solve_interior_tile(2, 2), "urullddruld",
                   "Test #5: first test for solve_interior_tile method")
    #print PuzzleBoard0
    suite.run_test(PuzzleBoard0.solve_interior_tile(2, 1), "l",
                   "Test #6: second test for solve_interior_tile method")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard1.solve_interior_tile(2, 1), "uldruld",
                   "Test #7: third test for solve_interior_tile method")
    #print PuzzleBoard1
    suite.run_test(PuzzleBoard3.solve_interior_tile(2, 1), "uurdlulddruld",
                   "Test #8: fourth test for solve_interior_tile method")
    print PuzzleBoard3
    suite.run_test(PuzzleBoard4.solve_interior_tile(2, 3), "lllurrdlurrdl",
                   "Test #9: fifth test for solve_interior_tile method")
    #print PuzzleBoard4
    suite.run_test(PuzzleBoard4.solve_interior_tile(2, 2), "uulldrruldrulddruld",
                   "Test #10: sixth test for solve_interior_tile method")
    #print PuzzleBoard4
    suite.run_test(PuzzleBoard5.solve_interior_tile(2, 2), "uulldrruldrulddruld",
                   "Test #11: last test for solve_interior_tile method")
    print PuzzleBoard5
    suite.run_test(PuzzleBoard5.solve_interior_tile(2, 1), "uulddruld",
                   "Test #12: last test for solve_interior_tile method")
    print PuzzleBoard5
    
    # testing the solve_col0_tile method
    print "###solve_col0_tile###"
    suite.run_test(PuzzleBoard0.solve_col0_tile(2), "uurrrdllurdluldruldrdlurdluurddlurrr",
                   "Test #13: first test for solve_col0_tile method")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard3.solve_col0_tile(2), "uurdlruldrdlurdluurddlurrr",
                   "Test #14: second test for solve_col0_tile method")
    print PuzzleBoard3
    suite.run_test(PuzzleBoard6.solve_col0_tile(2), "uurldruldruldrdlurdluurddlurrr",
                   "Test #15: third test for solve_col0_tile method")
    print PuzzleBoard6
    
    # testing the row0_invariant method
    print "###row0_invariant###"
    init_board = [[4, 2, 0, 3], [5, 1, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard7 = solver.Puzzle(4, 4, init_board)
    init_board = [[4, 2, 0, 6], [5, 1, 3, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard8 = solver.Puzzle(4, 4, init_board)

    print PuzzleBoard7
    suite.run_test(PuzzleBoard7.row0_invariant(2), True, "Test #16: first test for row0_invariant method")
    print PuzzleBoard8
    suite.run_test(PuzzleBoard8.row0_invariant(2), False, "Test #17: second test for row0_invariant method")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard0.row0_invariant(3), False, "Test #18: third test for row0_invariant method")
    
    # testing the row1_invariant method
    print "###row1_invariant###"
    init_board = [[4, 6, 1, 3], [5, 2, 0, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard9 = solver.Puzzle(4, 4, init_board)
    init_board = [[4, 6, 1, 7], [5, 2, 0, 3], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard10 = solver.Puzzle(4, 4, init_board)

    print PuzzleBoard0
    suite.run_test(PuzzleBoard0.row1_invariant(3), True, "Test #19: first test for row1_invariant method")
    print PuzzleBoard9
    suite.run_test(PuzzleBoard9.row1_invariant(2), True, "Test #20: second test for row1_invariant method")
    print PuzzleBoard10
    suite.run_test(PuzzleBoard10.row1_invariant(3), False, "Test #21: third test for row1_invariant method")
    
    # testing the solve_row1_tile method
    print "###solve_row1_tile###"
    init_board = [[7, 6, 1, 3], [5, 2, 4, 0], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard11 = solver.Puzzle(4, 4, init_board)
    init_board = [[5, 6, 1, 3], [7, 2, 4, 0], [8, 9, 10, 11], [12, 13, 14, 15]]
    PuzzleBoard12 = solver.Puzzle(4, 4, init_board)

    suite.run_test(PuzzleBoard0.solve_row1_tile(3), "u",
                   "Test #22: first test for solve_row1_tile method")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard11.solve_row1_tile(3), "ullldrurdlurrdlur",
                   "Test #23: second test for solve_row1_tile method")
    print PuzzleBoard11
    suite.run_test(PuzzleBoard12.solve_row1_tile(3), "lllurrdlurrdlur",
                   "Test #24: third test for solve_row1_tile method")
    print PuzzleBoard12
    
    # testing the solve_row0_tile method
    print "###solve_row0_tile###"
    suite.run_test(PuzzleBoard0.solve_row0_tile(3), "ldlurdlurldurdlurrdluldrruld",
                   "Test #25: first test for solve_row0_tile method")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard11.solve_row0_tile(3), "ld",
                   "Test #26: second test for solve_row0_tile method")
    print PuzzleBoard11
    suite.run_test(PuzzleBoard12.solve_row0_tile(3), "lldurdlurrdluldrruld",
                   "Test #27: third test for solve_row0_tile method")
    print PuzzleBoard12
    
    print "###mixed test###"
    suite.run_test(PuzzleBoard12.solve_row1_tile(2), "ulldrurdlur",
                   "Test #28: fourth test for solve_row1_tile method")
    print PuzzleBoard12
    suite.run_test(PuzzleBoard12.solve_row0_tile(2), "lldurdlurrdluldrruld",
                   "Test #29: third test for solve_row0_tile method")
    print PuzzleBoard12
    
    # testing the solve_2x2 method
    print "###solve_2x2###"
    suite.run_test(PuzzleBoard12.solve_2x2(), "lurdlu",
                   "Test #30: test for solve_2x2 method")
    print PuzzleBoard12
    
    # testing the solve_puzzle method
    
    # example of a run_test call for poc_simpletest
    #suite.run_test(wrangler.remove_duplicates(word_list), ["a", "b", "ab", "ba"],
    #                                          "Test #1: testing remove_duplicates")
    
    # report number of tests and failures
    print
    suite.report_results()

run_suite()

