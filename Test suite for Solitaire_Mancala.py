"""
Template testing suite for Solitaire Mancala
"""

import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class()
    
    # add tests using suite.run_test(....) here

    # check the str and get_num_seeds methods (by Coursera)
    suite.run_test(str(game), str([0]), "Test #0: init")
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    game.set_board(config1)   
    suite.run_test(str(game), str([0, 5, 3, 1, 1, 0, 0]), "Test #1a: str")
    suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")    
    
    # my own tests for further methods
    config2 = [0, 1, 1, 1, 3, 6, 0]
    config3 = [20, 0, 0, 0, 0, 0, 0]
    config4 = [0, 1]
    config5 = [0, 1, 2, 3]
    config6 = [0, 1, 1, 3, 2, 4, 6]
    suite.run_test(game.is_game_won(), False, "Test #2a: is_game_won False")    
    game.set_board(config3)   
    suite.run_test(game.is_game_won(), True, "Test #2b: is_game_won True")    
    game.set_board(config2)   
    suite.run_test(game.is_legal_move(5), False, "Test #3a: is_legal_move False")    
    suite.run_test(game.is_legal_move(4), False, "Test #3b: is_legal_move False")    
    suite.run_test(game.is_legal_move(1), True, "Test #3c: is_legal_move True")    
    game.set_board(config4)   
    suite.run_test(game.is_game_won(), False, "Test #4a: is_game_won False")    
    game.apply_move(1)
    suite.run_test(str(game), str([0, 1]), "Test #4c: after apply_move")
    suite.run_test(game.is_game_won(), True, "Test #4d: is_game_won True")    
    game.set_board(config5)   
    game.apply_move(3)
    suite.run_test(str(game), str([0, 3, 2, 1]), "Test #4e: after apply_move")
    game.set_board(config2)   
    game.apply_move(4)
    suite.run_test(str(game), str([0, 6, 3, 1, 1, 1, 0]), "Test #4f: after apply_move")
    game.set_board(config1)   
    suite.run_test(game.choose_move(), 5, "Test #5a: choose_move 5")    
    game.set_board(config3)   
    suite.run_test(game.choose_move(), 0, "Test #5b: choose_move 0")    
    game.set_board(config6)   
    planned_moves = game.plan_moves()
    result = [1, 3, 1, 2, 1, 6, 1, 5, 1, 2, 1, 4, 1, 3, 1, 2, 1]
    suite.run_test(game.plan_moves(), result , "Test #6: plan_moves")    
    for num in range(len(planned_moves)):
        game.apply_move(planned_moves[num])
    suite.run_test(game.is_game_won(), True, "Test #7: is_game_won after planned_moves")    
    
    # report number of tests and failures
    suite.report_results()
