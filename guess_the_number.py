# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# import modules to be used in this program
import simplegui
import random
import math

# define global variables
int_guess = None
secret_number = None
max_range = 100
guesses_left = None

# helper function to start and restart the game
def new_game():
    """ This function starts a new game. """
    global max_range, secret_number, guesses_left
    secret_number = random.randrange(0, max_range)
    guesses_left = int(math.ceil(math.log(max_range, 2)))
    print "\nNew game started."
    out = "The range is [0," + str(max_range) + ")."
    print out
    out = "You have " + str(guesses_left) + " guesses to guess the number."
    print out
    
# define event handlers for control panel
def range100():
    """ This button handler changes the range to [0,100)
        and starts a new game. """
    global max_range, guesses_left
    max_range = 100
    new_game()

def range1000():
    """ This button handler changes the range to [0,1000)
        and starts a new game. """
    global max_range, guesses_left
    max_range = 1000
    new_game()
    
def input_guess(guess):
    """ This functions recieves the guesses and handles them. """
    global int_guess, max_range, secret_number, guesses_left
    
    # convert the string guess into an integer and handle strange input
    try :
        int_guess = int(guess)
    except :
        print "ERROR ===> Please always enter an integer"
        print "           Try again!"
        return
    if int_guess < 0 :
        print "ERROR ===> Please always enter a positive number"
        print "           Try again!"
        return
    if int_guess > max_range - 1 :    
        print "ERROR ===> Please always enter a number less then", max_range - 1
        print "           Try again!"
        return

    # print out the guess
    print "Your last guess is " + guess + "."

    # test the guess against the secret number and print a message
    guesses_left -= 1
    if int_guess < secret_number :
        print "HIGHER"
        if guesses_left == 0 :
            print "You have no guesses left:\nYou have LOST the game!"
            new_game()
        else :
            out = "You have " + str(guesses_left) + " guesses left to guess the number."
            print out
    elif int_guess > secret_number :
        print "LOWER"
        if guesses_left == 0 :
            print "You have no guesses left:\nYou have LOST the game!"
            new_game()
        else :
            out = "You have " + str(guesses_left) + " guesses left to guess the number."
            print out
    else :
        print "CORRECT!\nYou have WON the game!"
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 100, 200)

# register event handlers for control elements and start frame
frame.add_input("Please enter your next guess:", input_guess, 100)
frame.add_button("Range [0,100)", range100, 150)
frame.add_button("Range [0,1000)", range1000, 150)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
