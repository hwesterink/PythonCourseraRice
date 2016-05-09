"""
Testing suite for Yahtzee
"""

import poc_simpletest
import user41_9DeFtNExlu_6 as clicker_simulator

def run_suite():
    """
    Testing code for the methods and functions written for Cookie Clicker
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()    
    
    # tests for the Cookie Clicker methods and functions
    # testting object constructor and __str__ method
    game = clicker_simulator.ClickerState()
    print game

    # testing get_cookies, get_cps, get_time, and get_history methods
    suite.run_test(game.get_cookies(), 0.0, "Test #1: testing get_cookies")
    suite.run_test(game.get_cps(), 1.0, "Test #2: testing get_cps")
    suite.run_test(game.get_time(), 0.0, "Test #3: testing get_time")
    suite.run_test(game.get_history(), [(0.0, None, 0.0, 0.0)], "Test #4: testing get_history")

    # testing time_until, wait, buy_item
    suite.run_test(game.time_until(9.5), 10.0, "Test #5: testing time_until")
    game.wait(10.0)
    suite.run_test(game.get_cookies(), 10.0, "Test #6.1: testing wait")
    suite.run_test(game.get_cps(), 1.0, "Test #6.2: testing wait")
    suite.run_test(game.get_time(), 10.0, "Test #6.3: testing wait")
    game.buy_item("Test 7 item", 9.5, 1.0)
    suite.run_test(game.get_cookies(), 0.5, "Test #7.1: testing buy_item")
    suite.run_test(game.get_cps(), 2.0, "Test #7.2: testing buy_item")
    print game
    
    # testing
    
    # testing wait
    game.wait(10.0)
    
    
    # report number of tests and failures
    suite.report_results()

run_suite()
