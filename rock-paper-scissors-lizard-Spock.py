
# IMPORT FUNCTION PACKAGES USED IN THIS MINI-PROJECT 

import random

# HELPER FUNCTIONS

def name_to_number(name):

    """
    The function name_to_number converts the names of
    rock-paper-scissors-lizard-Spock into numbers using the following
    table:
        0 = rock
        1 = Spock
        2 = paper
        3 = lizard
        4 = scissors
    """

    if name == "rock" :
        number = 0
    elif name == "Spock" :
        number = 1
    elif name == "paper" :
        number = 2
    elif name == "lizard" :
        number = 3
    elif name == "scissors" :
        number = 4
    else :
        print "===> Error in name_to_number: Wrong name entered -", name
        quit()
        
    return number

def number_to_name(number):

    """
    The function number_to_name converts the numbers 0 through 4
    into names using the following table:
        0 = rock
        1 = Spock
        2 = paper
        3 = lizard
        4 = scissors
    """

    if number == 0 :
        name = "rock"
    elif number == 1 :
        name = "Spock"
    elif number == 2 :
        name = "paper"
    elif number == 3 :
        name = "lizard"
    elif number == 4 :
        name = "scissors"
    else :
        print "===> Error in name_to_number: Wrong number entered -", number
        quit()
        
    return name
  

def rpsls(player_choice): 

    """
    The function rpsls plays the game rock-paper-scissors-lizard-Spock
    based on the player_choice entered. It prints the result as described
    in the requirements of the mini-project.
    """

    # print a blank line to separate consecutive games and
    # the message for the player's choice
    print "\nPlayer chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choise = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choise

    # compute difference of comp_number and player_number modulo five
    modulo_5 = (player_number - comp_number) % 5

    # use if/elif/else to determine winner, print winner message
    if modulo_5 == 0 :
        print "Player and computer tie!"
    elif modulo_5 == 1 or modulo_5 == 2 :
        print "Player wins!"
    else :
        print "Computer wins!"
    
# CALLS TO TEST THE FUNCTIONS
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
