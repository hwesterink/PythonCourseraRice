"""
Testing suite for Tic-Tac-Toe (Monte Carlo
"""

import poc_simpletest
import poc_ttt_provided as provided
import user41_sDIl7gUxIP_36 as ttt_functions

def run_suite(game_class):
    """
    Testing code for the functions written for Tic-Tac-Toe
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class(3, reverse = False, board = None)
    #print "Cells initially created:"
    #print game
    
    # partly fill the board to be an uncompleted game
    """
    game.move(1, 0, provided.PLAYERX); game.move(1, 1, provided.PLAYERX)
    game.move(2, 0, provided.PLAYERX)
    game.move(0, 0, provided.PLAYERO); game.move(1, 2, provided.PLAYERO)
    game.move(2, 0, provided.PLAYERO)
    """
    
    # preliminairy tests using suite.run_test(....)
    suite.run_test(game.check_win(), None, "Test #0.1: check_win on game in progress")
    #suite.run_test(game.get_empty_squares(),
    #               [(0, 1), (0, 2), (2, 1), (2, 2)], "Test #0.2: get_empty_squares")
    
    # testing mc_update_scores
    """
    scores = [ [0 for _dummy_col in range(3)]
                 for _dummy_row in range(3)]
    print scores
    game.move(0, 2, provided.PLAYERX); game.move(2, 2, provided.PLAYERO)
    suite.run_test(game.check_win(), provided.PLAYERX, "Test #1.1: check_win")
    suite.run_test(ttt_functions.mc_update_scores(scores, game, provided.PLAYERX),
                   None, "Test #1.2: mc_update_scores")
    print scores, "\nExpected: [[-1.0, 0, 1.0], [1.0, 1.0, -1.0], [1.0, 0, -1.0]]"
    suite.run_test(ttt_functions.mc_update_scores(scores, game, provided.PLAYERO),
                   None, "Test #1.3: mc_update_scores")
    print scores, "\nExpected: [[0.0, 0, 0.0], [0.0, 0.0, 0.0], [0.0, 0, 0.0]]"
    """

    # testing mc_trial
    #ttt_functions.mc_trial(game, provided.PLAYERX)
    game = game_class(2, reverse = False, board = None)
    ttt_functions.mc_trial(game, provided.PLAYERX)
    print game
    
    # testing mc_best_move
    """
    scores = [[1, 2, 3], [11, 12, 13], [21, 22, 23]]
    suite.run_test(ttt_functions.get_best_move(game, scores),
                   (2, 2), "Test #2.1: get_best_move")
    scores = [[1, 2, 3], [11, 50, 13], [21, 22, 23]]
    suite.run_test(ttt_functions.get_best_move(game, scores),
                   (1, 1), "Test #2.2: get_best_move")
    scores = [[1, 2, 50], [11, 12, 13], [21, 22, 23]]
    suite.run_test(ttt_functions.get_best_move(game, scores),
                   (0, 2), "Test #2.3: get_best_move")
    scores = [[1, 2, 3], [11, 12, 13], [50, 22, 23]]
    suite.run_test(ttt_functions.get_best_move(game, scores),
                   (2, 0), "Test #2.4: get_best_move")
    scores = [[-4.0, -5.0, 2.0], [3.0, 8.0, -3.0], [7.0, -4.0, 7.0]]
    print ttt_functions.get_best_move(game, scores)
    print "Expected (1, 1)"
    """
    
    # testing mc_move
    #print "\n", ttt_functions.mc_move(game, provided.PLAYERX, 25)
    
    # report number of tests and failures
    suite.report_results()

run_suite(provided.TTTBoard)    