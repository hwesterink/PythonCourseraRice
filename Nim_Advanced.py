"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random

MAX_REMOVE = 3
TRIALS = 10000
START_ITEMS = 24

def evaluate_pos_beginner(num_items):
    """
    Simple evalation method for Nim based on random computer moves
    """
    selected_remove = random.randrange(MAX_REMOVE)+1
    if selected_remove > num_items:
        selected_remove = num_items
    return selected_remove

def evaluate_pos_intermediate(num_items):
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

def evaluate_pos_expert(num_items):
    """
    Evalation method for Nim based on the optimal stategy
    """
    selected_remove = num_items % 4
    if selected_remove == 0:
        selected_remove = random.randrange(1,MAX_REMOVE+1)
    return selected_remove

def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    # Ask for playing mode
    output_string = ("What level do you want to play?\n" +
                     "b = Beginner.\ni = Intermediate\ne = Expert" +
                     "\n==> ")
    while True:
        player_mode = raw_input(output_string)
        if player_mode == "b" or player_mode == "i" or player_mode == "e":
            break
        elif player_mode == "":
            quit()
        else:
            if not(output_string.startswith("Invalid input!")):
                output_string = "Invalid input! Select 'b', 'i' or 'e'.\n\n" + output_string
    # Play game in selectede mode                             
    print "Starting game with value", current_items
    while True:
        if player_mode == "b":
            comp_move = evaluate_pos_beginner(current_items)
        elif player_mode == "i":
            comp_move = evaluate_pos_intermediate(current_items)
        else:
            comp_move = evaluate_pos_expert(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        output_string = "Enter your current move: "
        while True:
            player_move = raw_input(output_string)
            if player_move == "1" or player_move == "2" or player_move == "3":
                break
            elif player_move == "":
                quit()
            else:
                if not(output_string.startswith("Invalid input!")):
                    output_string = "Invalid input! Select '1', '2' or '3'.\n\n" + output_string
        current_items -= int(player_move)
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(START_ITEMS)
 