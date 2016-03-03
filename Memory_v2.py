# implementation of card game - Memory

# IMPORT THE MODULE(S)
import simplegui
import random

# IMPORT PICTURES FROM THE INTERNET AND SET DIMENSIONS
images = {}
SOURCE_PICT_DIMS = {}
images[0] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o1.jpg"))
SOURCE_PICT_DIMS[0] = [(50, 50), (100, 100)]
images[1] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o2.jpg"))
SOURCE_PICT_DIMS[1] = [(50, 50), (100, 100)]
images[2] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o3.jpg"))
SOURCE_PICT_DIMS[2] = [(50, 50), (100, 100)]
images[3] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o4.jpg"))
SOURCE_PICT_DIMS[3] = [(50, 50), (100, 100)]
images[4] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o5.jpg"))
SOURCE_PICT_DIMS[4] = [(50, 50), (100, 100)]
images[5] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o6.jpg"))
SOURCE_PICT_DIMS[5] = [(50, 50), (100, 100)]
images[6] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o7.jpg"))
SOURCE_PICT_DIMS[6] = [(50, 50), (100, 100)]
images[7] = (simplegui.load_image(
        "http://lidadijkstra.nl/illustraties/boeken-nederlands/o8.jpg"))
SOURCE_PICT_DIMS[7] = [(50, 50), (100, 100)]

# DEFINE AND INITIALIZE GLOBAL VARIABLES
# These global constants make it possible to vary the number of cards
# in the deck by changing HORIZONTAL_CARDS and VERTICAL_CARDS; make sure
# you specify an even number of cards. You can also adapt the card
# dimensions with CARD_WIDTH and CARD_HEIGHT. If the number of cards
# or the card size is changed the canvas is adapted to these changes.
HORIZONTAL_CARDS = 8
VERTICAL_CARDS = 2
CARD_WIDTH = 100
CARD_HEIGHT = 100
CANVAS_WIDTH = HORIZONTAL_CARDS * CARD_WIDTH
CANVAS_HEIGHT = VERTICAL_CARDS * CARD_HEIGHT
CARDS = HORIZONTAL_CARDS * VERTICAL_CARDS

# DEFINE "HELPERS" FUNCTIONS
def new_game():
# helper function to start a new game
    global deck, exposed, state, turns
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    deck = (range(HORIZONTAL_CARDS * VERTICAL_CARDS / 2) + 
            range(HORIZONTAL_CARDS * VERTICAL_CARDS / 2))
    random.shuffle(deck)
    exposed = []
    for i in range(CARDS) :
        exposed.append(False)

def centre_grid():
# helper function that computes the centres of the images
    global HORIZONTAL_CARDS, CARD_WIDTH, CARD_HEIGHT
    global pos_centre
    pos_centre = []
    for i in range(CARDS) :
        rest = i % HORIZONTAL_CARDS
        div = i // HORIZONTAL_CARDS
        positie = ( (CARD_WIDTH / 2.0 + rest * CARD_WIDTH),
                   (CARD_HEIGHT / 2.0 + div * CARD_HEIGHT))
        pos_centre.append(positie)
        
def cards_grid():
# helper function that computes the corners of the cards
    global HORIZONTAL_CARDS, VERTICAL_CARDS, CARD_WIDTH, CARD_HEIGHT
    global pos_corners
    pos_corners = {}
    pos_grid = []
    numb_corners = (HORIZONTAL_CARDS + 1) * (VERTICAL_CARDS + 1)
    for i in range(numb_corners) :
        rest = i % (HORIZONTAL_CARDS + 1)
        div = i // (HORIZONTAL_CARDS + 1)
        positie = ( rest * CARD_WIDTH, div * CARD_HEIGHT)
        pos_grid.append(positie)
    for i in range(CARDS) :
        rest = i % HORIZONTAL_CARDS
        div = i // HORIZONTAL_CARDS
        first = (HORIZONTAL_CARDS + 1) * div + rest
        last = first + HORIZONTAL_CARDS + 2
        corners = [pos_grid[first], pos_grid[first + 1], 
                   pos_grid[last], pos_grid[last - 1]]
        pos_corners[i] = corners
    
# DEFINE EVENT HANDLER FUNCTIONS
def mouseclick(pos):
# when the mouse is clicked the clicked card is flipped according
# to the rules of the game
    global CARDS, HORIZONTAL_CARDS, CARD_WIDTH, CARD_HEIGHT
    global exposed, state, turns
    global flipped1, flipped2
    for i in range(CARDS) :
        rest = i % HORIZONTAL_CARDS
        div = i // HORIZONTAL_CARDS
        width_range = [ rest * CARD_WIDTH, rest * CARD_WIDTH + CARD_WIDTH ]
        height_range = [ div * CARD_HEIGHT, div * CARD_HEIGHT + CARD_HEIGHT ]
        # detect which card is clicked and flip it over when hidden
        if ((pos[0] >= width_range[0] and pos[0] < width_range[1]) and
            (pos[1] >= height_range[0] and pos[1] < height_range[1])) :
            if not exposed[i] :
                exposed[i] = True
                # game state logic for the mouse click
                if state == 0 :
                    flipped1 = i
                    state = 1
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                elif state == 1 :
                    flipped2 = i
                    state = 2
                else :
                    if deck[flipped1] != deck[flipped2] :
                        exposed[flipped1] = False
                        exposed[flipped2] = False
                    state = 1
                    flipped1 = i
                    turns += 1
                    label.set_text("Turns = " + str(turns))
                           
def draw(canvas):
# the canvas with cards and flipped cards is drawn
    global images, SOURCE_PICT_DIMS, CARD_WIDTH, CARD_HEIGHT
    global exposed, deck, pos_centre, pos_corners
    for i in range(CARDS) :
        if exposed[i] :
            canvas.draw_image(images[deck[i]], SOURCE_PICT_DIMS[deck[i]][0],	
                              SOURCE_PICT_DIMS[deck[i]][1], pos_centre[i], 
                              (CARD_WIDTH, CARD_HEIGHT))
        else :
            canvas.draw_polygon(pos_corners[i], 2, "Red", "Green")

# CREATE FRAME
frame = simplegui.create_frame("Memory", CANVAS_WIDTH, CANVAS_HEIGHT)

# CREATE LABEL(S)
label = frame.add_label("Turns = 0")

# REGISTER EVENT HANDLERS
frame.add_button("Reset", new_game)
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# CREATE THE GRIDS NEEDED FOR THE GAME
centre_grid()
cards_grid()

# START GAME, FRAME AND TIMERS
new_game()
frame.start()


# Always remember to review the grading rubric