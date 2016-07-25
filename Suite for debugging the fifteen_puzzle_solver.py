"""
Debugging suite for methods developed for Fifteen Puzzle Solver
"""

import poc_simpletest
import user41_rJZfIie72I_115 as solver

def run_suite():
    """
    Testing code for the methods written for the Fifteen Puzzle solver
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()
    
    # create scrumbled boards to test the solver methods with
    init_board = [[15, 16, 0, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [1, 2, 17, 18, 19]]
    PuzzleBoard0 = solver.Puzzle(4, 5, init_board)
    print PuzzleBoard0
    print
    init_board = [[10, 5, 7, 3, 4], [1, 2, 6, 8, 9], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
    PuzzleBoard1 = solver.Puzzle(4, 5, init_board)
    print PuzzleBoard1
    print
    init_board = [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
    PuzzleBoard2 = solver.Puzzle(4, 5, init_board)
    print PuzzleBoard2
    init_board = [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]]
    PuzzleBoard3 = solver.Puzzle(4, 5, init_board)
    print PuzzleBoard3
    init_board = [[8, 2, 10, 9, 1], [7, 6, 5, 4, 3], [0, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
    PuzzleBoard4 = solver.Puzzle(4, 5, init_board)
    print PuzzleBoard4
    init_board = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
    PuzzleBoard5 = solver.Puzzle(3, 3, init_board)
    print PuzzleBoard5
    
    # testing the solve_interior_tile method
    suite.run_test(PuzzleBoard0.solve_puzzle(), "lddduuurdlulddrulddrulduuurldrulddruldruldrdlurdluurddlurrrrlllluurdlruldrdlurdluurddlurrrrlurldlurldullrdlurldurdlurrdluldrruldlurdlu",
                   "Test: debugging solve puzzle")
    print PuzzleBoard0
    suite.run_test(PuzzleBoard1.solve_puzzle(), "uurdlruldrdlurdluurddlurrrrlurldlurldullrdlurldurdlurrdluldrruldlurdlu",
                   "Test: debugging solve puzzle")
    print PuzzleBoard1
    suite.run_test(PuzzleBoard2.solve_col0_tile(2), "uurrdluldruldrdlurdluurddlurrrr",
                   "Test: debugging solve_col0_tile")
    print PuzzleBoard2
    print
    suite.run_test(PuzzleBoard3.solve_col0_tile(3), "uuurrrrdllurdllurdlulddruldruldrdlurdluurddlurrrr",
                   "Test: debugging solve_col0_tile")
    print PuzzleBoard3
    suite.run_test(PuzzleBoard4.solve_col0_tile(2), "uurrdluldruldrdlurdluurddlurrrr",
                   "Test: debugging solve_col0_tile")
    print PuzzleBoard4
    print
    suite.run_test(PuzzleBoard5.solve_puzzle(), "uulldrruldrulddrulduulddrulduurrdluldruldrdlurdluurddlurrllurrdlurldlu",
                   "Test: debugging solve puzzle")
    print PuzzleBoard5
    print
    
    # report number of tests and failures
    print
    suite.report_results()

run_suite()

