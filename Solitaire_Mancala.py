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
        if (self._content[house_num] != house_num) or house_num == 0:
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
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"
    
    config1 = [0, 0, 1, 1, 3, 5, 0]
#    config1 = [0, 1, 1, 1, 3, 6, 0]
#    config1 = [20, 0, 0, 0, 0, 0, 0]
#    config1 = [0, 1]
#    config1 = [0, 1, 2, 3]
    my_game.set_board(config1)   
    
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing is_game_won: - Computed:", my_game.is_game_won(), "Expected: False"
    print "Testing is_legal_move: - Computed:", my_game.is_legal_move(1), "Expected: False"
    print "Testing is_legal_move: - Computed:", my_game.is_legal_move(4), "Expected: False"
    print "Testing is_legal_move: - Computed:", my_game.is_legal_move(5), "Expected: True"
    my_game.apply_move(5)
    print "Testing apply_move - Computed:", str(my_game), "Expected:", str([0, 0, 4, 2, 2, 1, 1])
    print "Testing choose_move - Computed:", my_game.choose_move(), "Expected:", 1
    planned = my_game.plan_moves()
    print "Testing plan_moves - Computed:", str(planned), "Expected:", str([1, 2, 1, 4, 1, 3, 1, 2, 1])
    print "Computed end board is:", str(my_game)
    config2 = [0, 1, 2, 3, 4, 5, 6]
    my_game.set_board(config2)
    print "Testing set_board - Computed:", str(my_game), "Expected:", str([6, 5, 4, 3, 2, 1, 0])
    
#test_mancala()


# Import GUI code once you feel your code is correct
#import poc_mancala_gui
#poc_mancala_gui.run_gui(SolitaireMancala())
