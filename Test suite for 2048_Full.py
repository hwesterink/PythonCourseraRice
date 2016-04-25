"""
Template testing suite for Solitaire Mancala
"""


import poc_simpletest

def run_suite(game_class):
    """
    Some informal testing code
    """
    
    # Constants used to test move
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # create a game
    game = game_class(4,4)
    print "Cells initially created:"
    print game
    
    # add tests using suite.run_test(....) here

    # test the get_grid_height and grid_width methods
    suite.run_test(game.get_grid_height(), 4, "Test #1: get_grid_hight")
    suite.run_test(game.get_grid_width(), 4, "Test #2: get_grid_width")
    
    # test the set_tile and get_tile methods
    game.set_tile(3, 3, 16)
    print "Cells after game.set_tile(2, 4, 16)"
    print game
    suite.run_test(game.get_tile(3, 3), 16, "Test #3: get_tile after set_tile")
    
    # test the move method
    game.move(UP)
    print "Cells after game.move(UP)"
    print game
    game.move(LEFT)
    print "Cells after game.move(LEFT)"
    print game
    game.move(DOWN)
    print "Cells after game.move(DOWN)"
    print game
    game.move(RIGHT)
    print "Cells after game.move(RIGHT)"
    print game
    
    # report number of tests and failures
    suite.report_results()

    