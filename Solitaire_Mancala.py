"""
Implementation of solitaire version of Mancala - Tchoukaillon
Goal: Move as many seeds from given houses into the store
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self._content = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self._content = configuration
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        _reverse_list = list(self._content)
        _reverse_list.reverse()
        return str(_reverse_list)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self._content[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        for num in range(1,len(self._content)):
            if (self._content[num] != 0):
                return False
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        if (self._content[house_num] != house_num):
            return False
        return True

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if (self.is_legal_move(house_num)):
            self._content[house_num] = 0
            for num in range(house_num):
                self._content[num] += 1
        else:
            print "Illegal move."

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        for num in range(1,len(self._content)):
            if (self._content[num] == num):
                return num
        return 0
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
        After each move, move the seeds in the house closest to the store 
        when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        _planned_moves = []
        _reset_content = list(self._content)
        while True:
            if self.is_game_won():
                break
            _next_move = self.choose_move()
            if _next_move == 0:
                break
            _planned_moves.append(_next_move)
            self.apply_move(_next_move)
        self._content = _reset_content
        return _planned_moves
 

# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())


# Import test suite and run
import user41_acBbdmBrvs_14 as poc_mancala_testsuite
poc_mancala_testsuite.run_suite(SolitaireMancala)    
