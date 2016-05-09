"""
Planner for Yahtzee

30-4-2016:      Version 1: 
                Simplifications:    only allow discard and roll,
                                    only score against upper level
"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

# HELPER FUNCTIONS FOR THE YAHTZEE STRATEGY PLANNER

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

# Helper funcions that create sequenses of hold tuples of a given length

def length_one_tuples(hand, length):
    """
    Create the tuples to hold of length one
    """
    _new_holds = set()
    for _idx in range(length):
        _new_holds.add(tuple([hand[_idx]]))
    return _new_holds

def length_two_tuples(hand, length):
    """
    Create the tuples to hold of length two
    """
    _new_holds = set()
    for _idx1 in range(length-1):
        for _idx2 in range(_idx1+1,length):
            _new_holds.add(tuple([hand[_idx1], hand[_idx2]]))
    return _new_holds

def length_three_tuples(hand, length):
    """
    Create the tuples to hold of length three
    """
    _new_holds = set()
    for _idx1 in range(length-2):
        for _idx2 in range(_idx1+1,length-1):
            for _idx3 in range(_idx2+1,length):
                _new_holds.add(tuple([hand[_idx1], hand[_idx2], hand[_idx3]]))
    return _new_holds

def length_four_tuples(hand, length):
    """
    Create the tuples to hold of length four
    """
    _new_holds = set()
    for _idx1 in range(length-3):
        for _idx2 in range(_idx1+1,length-2):
            for _idx3 in range(_idx2+1,length-1):
                for _idx4 in range(_idx3+1,length):
                    _new_holds.add(tuple([hand[_idx1], hand[_idx2], hand[_idx3], hand[_idx4]]))
    return _new_holds

def length_five_tuples(hand, length):
    """
    Create the tuples to hold of length five
    """
    _new_holds = set()
    for _idx1 in range(length-4):
        for _idx2 in range(_idx1+1,length-3):
            for _idx3 in range(_idx2+1,length-2):
                for _idx4 in range(_idx3+1,length-1):
                    for _idx5 in range(_idx4+1,length):
                        _new_holds.add(tuple([hand[_idx1], hand[_idx2], hand[_idx3],
                                       hand[_idx4], hand[_idx5]]))
    return _new_holds

def length_six_tuples(hand, length):
    """
    Create the tuples to hold of length six
    """
    _new_holds = set()
    for _idx1 in range(length-5):
        for _idx2 in range(_idx1+1,length-4):
            for _idx3 in range(_idx2+1,length-3):
                for _idx4 in range(_idx3+1,length-2):
                    for _idx5 in range(_idx4+1,length-1):
                        for _idx6 in range(_idx5+1,length):
                            _new_holds.add(tuple([hand[_idx1], hand[_idx2], hand[_idx3],
                                           hand[_idx4], hand[_idx5], hand[_idx6]]))
    return _new_holds


# FUNCTIONS THAT DETERMINE THE YAHTZEE STRATEGY

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer maximum score for the hand based on the
    best choice in the upper section of the Yahtzee score card.
    """
    _maximum = 0
    _sub_total = 0
    _previous = 0
    for _idx in range(len(hand)):
        if _previous == hand[_idx]:
            _sub_total += hand[_idx]
        else:
            if _maximum < _sub_total:
                _maximum = _sub_total
            _sub_total = hand[_idx]
            _previous = hand[_idx]
    if _maximum < _sub_total:
        _maximum = _sub_total    
    return _maximum


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    _outcomes = [_idx for _idx in range(1,num_die_sides+1)]
    _sequences_rolled = gen_all_sequences(_outcomes, num_free_dice)
    _held_dice = list(held_dice)
    _total_score = 0
    for _sequence in _sequences_rolled:
        _seq_list = list(_sequence)
        _dice = list(held_dice)
        _dice.extend(_seq_list)
        _dice.sort()
        _total_score += score(_dice)
    return float(_total_score) / len(_sequences_rolled)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    _length = len(hand)
    # generate empty tuple
    _all_holds = set([()])
    # generate tuples of length one
    if _length > 0:
        _all_holds = _all_holds.union(length_one_tuples(hand, _length))
    # generate tuples of length two
    if _length > 1:
        _all_holds = _all_holds.union(length_two_tuples(hand, _length))
    # generate tuples of length three
    if _length > 2:
        _all_holds = _all_holds.union(length_three_tuples(hand, _length))
    # generate tuples of length four
    if _length > 3:
        _all_holds = _all_holds.union(length_four_tuples(hand, _length))
    # generate tuples of length five
    if _length > 4:
        _all_holds = _all_holds.union(length_five_tuples(hand, _length))
    # generate tuples of length six
    if _length > 5:
        _all_holds = _all_holds.union(length_six_tuples(hand, _length))
    return _all_holds


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    # Determine the possible holds for the provided hand and initialize
    _holds = gen_all_holds(hand)
    _selected_hold = None
    _max_expected_value = 0
    # Compute the expected value for all holds and find the hold
    # with the highest expected value
    for _hold in _holds:
        _num_free_dice = len(hand) - len(_hold)
        _expected_value = expected_value(_hold, num_die_sides, _num_free_dice)
        if _expected_value > _max_expected_value:
            _max_expected_value = _expected_value
            _selected_hold = tuple(_hold)
    # Produce the output and return it
    _result = tuple([_max_expected_value, _selected_hold])
    return _result


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
