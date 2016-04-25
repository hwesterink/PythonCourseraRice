"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    best_perc = 0.0
    best_remove = 0
    # Loop through all possible first moves
    for first_move in range(1,MAX_REMOVE+1):
        wins = 0
        losses = 0
    # Compute the percentage wins for the first_move selected
        for _dummy in range(TRIALS):
            total = first_move
            win = True
            while total < num_items:
                total += random.randrange(1,MAX_REMOVE+1)
                win = not win
            if win:
                wins += 1
        current_perc = float(wins) / TRIALS
    # Select best_move with the highest percentage wins
        if best_perc < current_perc:
            best_perc = current_perc
            best_remove = first_move
    return best_remove


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(15)
        
    
                 
    