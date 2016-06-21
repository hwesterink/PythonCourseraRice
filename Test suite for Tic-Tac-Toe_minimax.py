"""
Testing suite for functions developed for Tic-Tac-Toe MiniMax
"""

import poc_simpletest
import poc_ttt_provided as provided
import user41_SgYkRZCB69_5 as TTT

def run_suite():
    """
    Testing code for the function written for Tic-Tac-Toe MiniMax
    """
    
    # create a TestSuite (and an object)
    suite = poc_simpletest.TestSuite()
    
    # create a partially filled board to test the mm_move function
    game = provided.TTTBoard(3, reverse = False, board = None)
    game.move(0, 0, provided.PLAYERO)
    game.move(1, 0, provided.PLAYERO)
    game.move(0, 1, provided.PLAYERX)
    game.move(1, 1, provided.PLAYERX)
    game.move(2, 1, provided.PLAYERO)
    game.move(2, 2, provided.PLAYERX)
    game_save = game.clone()
    print game
    
    # testing the mm_move function
    game.move(2, 0, provided.PLAYERX)
    suite.run_test(TTT.mm_move(game, provided.PLAYERO), (0, (0, 2)),
                   "Test #1: testing the first board situation")
    game = game_save.clone()
    game.move(0, 2, provided.PLAYERX)
    suite.run_test(TTT.mm_move(game, provided.PLAYERO), (-1, (2, 0)),
                   "Test #2: testing another board situation")
    game = game_save.clone()
    game.move(1, 2, provided.PLAYERX)
    suite.run_test(TTT.mm_move(game, provided.PLAYERO), (-1, (2, 0)),
                   "Test #3: testing another board situation")
    game = game_save.clone()
    suite.run_test(TTT.mm_move(game, provided.PLAYERX), (0, (2, 0)),
                   "Test #4: testing a larger board situation")
    
    # example of a run_test call for poc_simpletest
    #suite.run_test(wrangler.remove_duplicates(word_list), ["a", "b", "ab", "ba"],
    #                                          "Test #1: testing remove_duplicates")
    
    # report number of tests and failures
    print
    suite.report_results()

run_suite()
