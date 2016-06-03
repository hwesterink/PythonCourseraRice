"""
Testing suite for Zombie Apocalypse
"""

import poc_simpletest
import user41_4hamr96US0_36 as za

def run_suite():
    """
    Testing code for the methods written for Zombie Apocalypse
    """
    
    # create a TestSuite and aa Apocalypse object
    suite = poc_simpletest.TestSuite()
    obstacles = [(0, 1), (3, 3), (5, 2)]
    humans = [(0, 0), (1, 2), (2, 2)]
    zombies = [(1, 1), (2, 2), (5, 3)]
    zombies_game = za.Apocalypse(6, 4, obstacles, zombies, humans)
    """
    print zombies_game
    print zombies_game._human_list
    print zombies_game._zombie_list
    print
    
    # tests for the Apocalypse clear method
    zombies_game.clear()
    print zombies_game
    print zombies_game._human_list
    print zombies_game._zombie_list
    print
    
    # tests for the Apocalypse add_zombie and num_zombies methods
    zombies_game.add_zombie(1, 1)
    zombies_game.add_zombie(2, 2)
    zombies_game.add_zombie(3, 3)
    print zombies_game._zombie_list
    suite.run_test(zombies_game.num_zombies(), 3, "Test #1: testing num_zombies")
    
    # test the Apocalypse humans generator method
    genres = zombies_game.zombies()
    print genres.next()
    print genres.next()
    print genres.next()
    print genres.next()
    
    # tests for the Apocalypse add_human and num_humans methods
    zombies_game.add_human(5, 3)
    zombies_game.add_human(4, 2)
    print zombies_game._human_list
    suite.run_test(zombies_game.num_humans(), 2, "Test #2: testing num_humans")
    
    # test the Apocalypse humans generator method
    genres = zombies_game.humans()
    print genres.next()
    print genres.next()
    print genres.next()
    """

    # first test the of the Apocalypse distance_field method
    zombie_distances = zombies_game.compute_distance_field(za.ZOMBIE)
    print zombies_game._human_list
    print zombie_distances
    zombies_game.move_humans(zombie_distances)
    print zombies_game._human_list
    print
    human_distances = zombies_game.compute_distance_field(za.HUMAN)
    print zombies_game._zombie_list
    print human_distances
    zombies_game.move_zombies(human_distances)
    print zombies_game._zombie_list
    
    # report number of tests and failures
    print
    suite.report_results()

run_suite()
