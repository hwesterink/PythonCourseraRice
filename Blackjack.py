# Mini-project #6 - Blackjack

# IMPORT THE MODULE(S)
import simplegui
import random


# IMPORT CARDS AND CARD BACK SIDE
# card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image(
    "http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    


# DEFINE AND INITIALIZE GLOBAL VARIABLES
in_play = False
outcome = ""
score = 0


# DEFINE CLASSES
# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
                             '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE,
                    [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        string = " contains:\n"
        for card in self.cards:
            rank = card.get_rank()
            if rank == "A": string += "Ace of "
            elif rank == "T": string += "10 of "
            elif rank == "J": string += "Jack of "
            elif rank == "Q": string += "Queen of "
            elif rank == "K": string += "King of "
            else: string += rank + " of "
            suit = card.get_suit()
            if suit == "C": string += "Clubs.\n"
            elif suit == "S": string += "Spades.\n"
            elif suit == "H": string += "Hearts.\n"
            else: string += "Diamonds.\n"
        return string

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if
        # it doesn't bust
        global VALUES
        value = 0
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
        for card in self.cards:
            rank = card.get_rank()
            if rank == "A":
                if value <= 11:
                    value += 10
        return value

    def draw(self, canvas, pos):
        global back
        global CARD_BACK_CENTER, CARD_BACK_SIZE
        # draw a hand on the canvas, using the draw method for cards
        for card in self.cards:
            if back and in_play:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                    [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                     CARD_BACK_SIZE)
                back = False
            else:
                card.draw(canvas, pos)
            pos[0] += 82
    
# define deck class 
class Deck:
    def __init__(self):
        global SUITS, RANKS
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card = self.deck.pop(-1)
        return card
    
    def __str__(self):
        string = "Deck still contains:\n"
        counter = 0
        for card in self.deck:
            counter += 1
            rank = card.get_rank()
            if rank == "A": string += str(counter) + ". Ace of "
            elif rank == "T": string += str(counter) + ". 10 of "
            elif rank == "J": string += str(counter) + ". Jack of "
            elif rank == "Q": string += str(counter) + ". Queen of "
            elif rank == "K": string += str(counter) + ". King of "
            else: string += str(counter) + ". " + rank + " of "
            suit = card.get_suit()
            if suit == "C": string += "Clubs.\n"
            elif suit == "S": string += "Spades.\n"
            elif suit == "H": string += "Hearts.\n"
            else: string += "Diamonds.\n"
        string += "In total there are still " + str(counter) + " cards in the deck."
        return string


# DEFINE EVENT HANDLERS
def deal():
    global score, outcome, in_play
    global dealer_deck, dealer_hand, player_hand
    if in_play:
        outcome = "You lost the round! Hit or stand?"
        score -= 1
    else:
        outcome = "Hit or Stand?"
        dealer_deck = Deck()
    dealer_deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    in_play = True
    for i in range(2):
        card = dealer_deck.deal_card()
        player_hand.add_card(card)
        card = dealer_deck.deal_card()
        dealer_hand.add_card(card)

def hit():
    global score, outcome, in_play
    global dealer_deck, player_hand, player_value
    if in_play:
        player_value = player_hand.get_value()
        if player_value <= 21:
            card = dealer_deck.deal_card()
            player_hand.add_card(card)
            player_value = player_hand.get_value()
        if player_value > 21:
            outcome = "You have busted! New deal?"
            score -= 1
            in_play = False
       
def stand():
    global score, outcome, in_play
    global dealer_deck, dealer_hand, player_value
    player_value = player_hand.get_value()
    if player_value > 21:
        outcome = "You cann't!!! You have busted!"
    elif in_play:
        dealer_value = dealer_hand.get_value()
        while dealer_value < 17:
            card = dealer_deck.deal_card()
            dealer_hand.add_card(card)
            dealer_value = dealer_hand.get_value()
        if dealer_value > 21:
            outcome = "The dealer has busted! New deal?"
            score += 1
        elif player_value > dealer_value:
            outcome = "You have WON! New deal?"
            score += 1
        else:
            outcome = "You have lost! New deal?"
            score -= 1
    in_play = False
            
# draw handler    
def draw(canvas):
    global dealer_hand, player_hand
    global outcome, back
    canvas.draw_text("Blackjack", [225, 85], 70, "Blue")
    # draw the dealers hand
    canvas.draw_text("The dealer's hand:", [50, 150], 30, "Red")
    position = [50, 175]
    back = True
    dealer_hand.draw(canvas, position)
    # draw the players hand
    canvas.draw_text("The player's hand:", [50, 350], 30, "Red")
    canvas.draw_text("Score: " + str(score), [550, 350], 50, "Orange")
    position = [50, 375]
    player_hand.draw(canvas, position)
    canvas.draw_text(outcome, [50, 540], 50, "Yellow")

                     
# CREATE FRAME
frame = simplegui.create_frame("Blackjack", 775, 600)
frame.set_canvas_background("Green")


# REGISTER EVENT HANDLERS
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# START FRAME
deal()
frame.start()


# remember to review the gradic rubric