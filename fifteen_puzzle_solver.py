"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui



#####################################
# Helper functions for the methods

def free_to_tile(func_in):
    """
    Helper function that moves the free tile to the target tile
    """
    move_string = func_in[0]
    target_col = func_in[2]
    zero_row = func_in[3]
    zero_col = func_in[4]
    tile_row = func_in[5]
    tile_col = func_in[6]
    
    while zero_row != tile_row:
        move_string += "u"
        zero_row -= 1
    if target_col == tile_col:
        tile_row += 1
    else:
        while zero_col != tile_col:
            if tile_col < zero_col:
                move_string += "l"
                zero_col -= 1
            else:
                move_string += "r"
                zero_col += 1
        if target_col < tile_col:
            tile_col -= 1
        else:
            tile_col += 1

    return move_string, zero_row, zero_col, tile_row, tile_col

def solve_tile(func_in):
    """
    Helper function that moves the target tile to the target field
    """
    func_in = tile_to_col(func_in)
    func_in = tile_to_row(func_in)
    
    move_string = func_in[0]
    zero_row = func_in[3]
    zero_col = func_in[4]
    tile_row = func_in[5]
    tile_col = func_in[6]

    return move_string, zero_row, zero_col, tile_row, tile_col

def tile_to_col(func_in):
    """
    Helper function that moves the target tile to the target column
    """
    move_string = func_in[0]
    target_row = func_in[1]
    target_col = func_in[2]
    zero_row = func_in[3]
    zero_col = func_in[4]
    tile_row = func_in[5]
    tile_col = func_in[6]
    
    # move the tile to the target column
    while target_col != tile_col:
        if tile_col < target_col:
            if tile_row == 0:
                move_string += "drrul"
            else:
                move_string += "urrdl"
            tile_col += 1
            zero_col += 1
        else:
            if tile_row == 0:
                move_string += "dllur"
            else:    
                move_string += "ulldr"
            tile_col -= 1
            zero_col -= 1

    return ( move_string, target_row, target_col, zero_row, zero_col, tile_row, tile_col )
        
def tile_to_row(func_in):
    """
    Helper function that moves the target tile to the target row
    """
    move_string = func_in[0]
    target_row = func_in[1]
    target_col = func_in[2]
    zero_row = func_in[3]
    zero_col = func_in[4]
    tile_row = func_in[5]
    tile_col = func_in[6]
    
    # move the tile to the target row
    if target_row != tile_row:
        if zero_col < tile_col:
            move_string += "dru"
            zero_col -= 1
        elif zero_col == tile_col:
            move_string += "lddru"
            zero_row += 1
        else:
            if tile_row == 0:
                move_string += "dlu"
                zero_col += 1
            else:
                move_string += "ullddru"
                zero_col -= 1
        tile_row += 1
        while target_row != tile_row:
            move_string += "lddru"
            tile_row += 1
            zero_row += 1
    if zero_row == target_row - 1:
        move_string += "ld"
        zero_col -= 1
        zero_row += 1
        
    return ( move_string, target_row, target_col, zero_row, zero_col, tile_row, tile_col )

def skip_placed_tiles(row_number, col_number, grid):
    """
    Helper function that skips tiles that are already in place
    """
    _stop = False
    _puzzle_width = col_number + 1
    while row_number >= 0 and not _stop:
        while col_number >= 0 and not _stop:
            if ( grid[row_number][col_number] !=
                _puzzle_width * row_number + col_number ):
                _stop = True
            if not _stop:
                col_number -= 1
        if not _stop:
            col_number = _puzzle_width - 1
            row_number -= 1
    return row_number, col_number


#####################################
# Definition of the Puzzle class

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        # check the position of the zero field
        if self._grid[target_row][target_col] != 0:
            return False

        # initialize variables
        _row_counter = target_row
        _col_counter = target_col + 1
        _max_row = self.get_height() - 1
        _max_col = self.get_width() - 1
        _col_width = self.get_width()

        # check positions after zero field
        while _row_counter <= _max_row:
            while _col_counter <= _max_col:
                if (self._grid[_row_counter][_col_counter] !=
                    ( _col_counter + _row_counter * _col_width )):
                    return False
                _col_counter += 1
            _col_counter = 0
            _row_counter += 1
            
        # reached invariant verified position
        return True
        
    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # check if the starting board complies to the lower_row_invariant
        assert self.lower_row_invariant(target_row, target_col), \
                "Starting board does not comply with lower_row_invariant"

        # check if the target position is an interior tile
        assert ( target_row > 1 and target_col > 0 ), \
                "Target position is not a interior tile"
        
        # initialize variables
        _move_string = ""
        _zero_row = target_row
        _zero_col = target_col
        _tile_position = self.current_position(target_row, target_col)
        _tile_row = _tile_position[0]
        _tile_col = _tile_position[1]
        
        # move the free position to the position of the selected tile
        _function_input = ( _move_string, target_row, target_col, _zero_row, _zero_col, _tile_row, _tile_col )
        _move_string, _zero_row, _zero_col, _tile_row, _tile_col = \
                        free_to_tile(_function_input)
                
        # move the tile to the target column and the target row and
        # place the free position on the new starting position
        _function_input = ( _move_string, target_row, target_col, _zero_row, _zero_col, _tile_row, _tile_col )
        _move_string, _zero_row, _zero_col, _tile_row, _tile_col = \
                        solve_tile(_function_input)
        
        # apply move string to the game board
        self.update_puzzle(_move_string)
        
        # check the resulting board against the lower_row_invariant
        assert self.lower_row_invariant(target_row, target_col-1), \
                "Solved board does not comply with lower_row_invariant"
        
        # return the string of moves needed to solve the tile
        return _move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # check if the starting board complies to the lower_row_invariant
        assert self.lower_row_invariant(target_row, 0), \
                "Starting board does not comply with lower_row_invariant"

        # check if the target position is an interior tile
        assert ( target_row > 1 ), "Target position is in row 0 or 1"
        
        # initialize variables
        _move_string = ""
        _zero_row = target_row
        target_col = 0
        _zero_col = 0
        _tile_position = self.current_position(target_row, 0)
        _tile_row = _tile_position[0]
        _tile_col = _tile_position[1]
        _last_col = self.get_width() - 1
        
        # move the free position to the position of the selected tile
        _function_input = ( _move_string, target_row, target_col, _zero_row,
                           _zero_col, _tile_row, _tile_col )
        _move_string, _zero_row, _zero_col, _tile_row, _tile_col = free_to_tile(_function_input)
            
        if (_tile_col != target_col) or (_tile_row != target_row):
            if _zero_col == 0:
                # move the selected tile to row 1
                _move_string += "rdl"
                _zero_row += 1
                _tile_col += 1
                if _tile_row != target_row - 1:
                    _move_string += "dru"
                    _zero_col += 1
                    _tile_row += 1
            elif _zero_col == 1:
                # move the selected tile to row 1
                _move_string += "l"
                _zero_col -= 1
                _tile_col += 1
                if _tile_row != target_row - 1:
                    _move_string += "dru"
                    _zero_col += 1
                    _tile_row += 1
                    if _tile_row == target_row - 1:
                        _move_string += "ld"
                        _zero_col -= 1
                        _zero_row += 1
            
            # drag the tile to the position directly above the last solved tile
            if ( _tile_row != target_row - 1 ) or ( _tile_col != 1 ):
                _function_input = ( _move_string, target_row - 1, 1, _zero_row,
                                  _zero_col, _tile_row, _tile_col )
                _move_string, _zero_row, _zero_col, _tile_row, _tile_col = solve_tile(_function_input)
            
            # move the tile to the target position
            _move_string += "ruldrdlurdluurddlur"
            _zero_col = 1

        # place the free position on the new starting position
        while _zero_col != _last_col:
            _move_string += "r"
            _zero_col += 1

        # apply move string to the game board
        self.update_puzzle(_move_string)
        
        # check the resulting board against the lower_row_invariant
        assert self.lower_row_invariant(target_row - 1, _last_col), \
                "Solved board does not comply with lower_row_invariant"
        
        # return the string of moves needed to solve the tile
        return _move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # check the position of the zero field
        if self._grid[0][target_col] != 0:
            return False

        # initialize variables
        _max_row = self.get_height() - 1
        _max_col = self.get_width() - 1
        _col_width = self.get_width()

        # check whether positions under row 1 are solved
        _row_counter = 2
        _col_counter = 0
        while _row_counter <= _max_row:
            while _col_counter <= _max_col:
                if (self._grid[_row_counter][_col_counter] !=
                    ( _col_counter + _row_counter * _col_width )):
                    return False
                _col_counter += 1
            _col_counter = 0
            _row_counter += 1
            
        # check whether positions to the right of the zero position are solved
        _row_counter = 0
        _col_counter = target_col + 1
        while _col_counter <= _max_col:
            if (self._grid[_row_counter][_col_counter] !=
                ( _col_counter + _row_counter * _col_width )):
                return False
            _col_counter += 1

        # check whether position in the row under the zero position
        # and to the right of that position are solved
        _row_counter = 1
        _col_counter = target_col
        while _col_counter <= _max_col:
            if ( self._grid[_row_counter][_col_counter] !=
                ( _col_counter + _row_counter * _col_width )):
                return False
            _col_counter += 1
                
        # reached invariant verified position
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # check the position of the zero field
        if self._grid[1][target_col] != 0:
            return False

        # initialize variables
        _max_row = self.get_height() - 1
        _max_col = self.get_width() - 1
        _col_width = self.get_width()

        # check whether positions under row 1 are solved
        _row_counter = 2
        _col_counter = 0
        while _row_counter <= _max_row:
            while _col_counter <= _max_col:
                if (self._grid[_row_counter][_col_counter] !=
                    ( _col_counter + _row_counter * _col_width )):
                    return False
                _col_counter += 1
            _col_counter = 0
            _row_counter += 1
            
        # check whether positions in the row above the zero position to the right are solved
        _row_counter = 0
        _col_counter = target_col + 1
        while _col_counter <= _max_col:
            if (self._grid[_row_counter][_col_counter] !=
                ( _col_counter + _row_counter * _col_width )):
                return False
            _col_counter += 1

        # check whether positions to the right of the zero position are solved
        _row_counter = 1
        _col_counter = target_col + 1
        while _col_counter <= _max_col:
            if (self._grid[_row_counter][_col_counter] !=
                ( _col_counter + _row_counter * _col_width )):
                return False
            _col_counter += 1
            
        # reached invariant verified position
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # check if the starting board complies to the row1_invariant
        assert self.row0_invariant(target_col), \
                "Starting board does not comply with row0_invariant"

        # check if the target position is outside the 2x2 puzzle
        assert ( target_col > 1 ), "Target position is not outside the 2x2 puzzle"
        
        # initialize variables
        _move_string = ""
        _zero_row = 0
        _zero_col = target_col
        _tile_position = self.current_position(0, target_col)
        _tile_row = _tile_position[0]
        _tile_col = _tile_position[1]
        
        _move_string += "l"
        _zero_col -= 1
        if _tile_row != 0 or _tile_col != _zero_col:
            # make a column with the zero tile above the target tile
            if _tile_row == 1:
                while _zero_col != _tile_col:
                    _move_string += "l"
                    _zero_col -= 1
            else:
                _move_string += "d"
                _zero_row += 1
                while _zero_col != _tile_col:
                    _move_string += "l"
                    _zero_col -= 1
                _move_string += "u"
                _zero_row -= 1
                _tile_row += 1
        
            # move the column to (target_col - 1), place the 0 zero tile before the target tile
            while _tile_col != target_col - 1:
                _move_string += "rdlur"
                _zero_col += 1
                _tile_col += 1
            _move_string += "ld"
            _zero_col -= 1
            _zero_row += 1
        
            # add the move string to solve the target tile
            _move_string += "urdlurrdluldrruld"
            _tile_col += 1
            _tile_row -= 1
            _zero_col += 1
        else:
            _move_string += "d"
            _zero_row += 1
        
        # apply move string to the game board
        self.update_puzzle(_move_string)
        
        # check the resulting board against the row0_invariant
        assert self.row1_invariant(target_col-1), \
                "Solved board does not comply with row1_invariant"
        
        # return the string of moves needed to solve the tile
        return _move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # check if the starting board complies to the row1_invariant
        assert self.row1_invariant(target_col), \
                "Starting board does not comply with row1_invariant"

        # check if the target position is outside the 2x2 puzzle
        assert ( target_col > 1 ), "Target position is not outside the 2x2 puzzle"
        
        # initialize variables
        _move_string = ""
        _zero_row = 1
        _zero_col = target_col
        _tile_position = self.current_position(1, target_col)
        _tile_row = _tile_position[0]
        _tile_col = _tile_position[1]
        
        # move the free position to the position of the selected tile
        _function_input = ( _move_string, 1, target_col, _zero_row, _zero_col, _tile_row, _tile_col )
        _move_string, _zero_row, _zero_col, _tile_row, _tile_col = \
                        free_to_tile(_function_input)
        
        if (_tile_col != target_col) or (_tile_row != 1):
            # move the tile to row 1 and zero tile right above it
            if _tile_row != 1:
                _move_string += "dru"
                _zero_col += 1
                _tile_row += 1
            else:
                _move_string += "ur"
                _zero_col += 1
                _zero_row -= 1
            # move the tile to the target place
            while _tile_col != target_col:
                _move_string += "rdlur"
                _zero_col += 1
                _tile_col += 1
        else:
            if _zero_row != 0:
                _move_string += "ur"
        
        # apply move string to the game board
        self.update_puzzle(_move_string)
        
        # check the resulting board against the row0_invariant
        assert self.row0_invariant(target_col), \
                "Solved board does not comply with row0_invariant"
        
        # return the string of moves needed to solve the tile
        return _move_string


    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # initialize variables
        _move_string = ""
        _col_width = self.get_width()
        _solved_poss = (0, 1, _col_width, _col_width + 1)
        _max_moves = 3

        # move the zero tile to the 0,0 position
        _move_string += "lu"
        self.update_puzzle("lu")
        
        # find the solved position
        for _dummy_index in range(_max_moves):
            if self._grid[0][0] == _solved_poss[0] and self._grid[0][1] == _solved_poss[1] and \
               self._grid[1][0] == _solved_poss[2] and self._grid[1][1] == _solved_poss[3]:
                return _move_string
            _move_string += "rdlu"
            self.update_puzzle("rdlu")

        # the puzzle is an insolvable variant
        assert False, "This is a puzzle that cannot be solved"

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # initialize variables
        _move_string = ""
        _puzzle_width = self.get_width()

        # skip trailing tiles that are already in place
        _row_number = self.get_height() - 1
        _col_number = self.get_width() - 1
        _grid = self._grid
        _row_number, _col_number = skip_placed_tiles(_row_number, _col_number, _grid)
        if _row_number == -1:
            print "The input puzzle is already solved!"
            return ""
        
        # move the zero tile right before the last tile that is in place
        _zero_position = self.current_position(0, 0)
        _zero_row = _zero_position[0]
        _zero_col = _zero_position[1]
        while _zero_col < _col_number:
            _move_string += "r"
            _zero_col += 1
        while _zero_col > _col_number:
            _move_string += "l"
            _zero_col -= 1
        while _zero_row < _row_number:
            _move_string += "d"
            _zero_row += 1
        self.update_puzzle(_move_string)
        
        # solve rows up to the third row
        while _row_number >= 2:
            while _col_number >= 0:
                if _col_number != 0:
                    _move_string += self.solve_interior_tile(_row_number, _col_number)
                else:
                    _move_string += self.solve_col0_tile(_row_number)
                _col_number -= 1
            _col_number = _puzzle_width - 1
            _row_number -= 1

        # solve the first two rows up to the third column
        while _col_number >= 2:
            _move_string += self.solve_row1_tile(_col_number)
            _move_string += self.solve_row0_tile(_col_number)
            _col_number -= 1
        
        # solve the last 2x2 puzzle
        _move_string += self.solve_2x2()
        
        # return the string of moves needed to solve the whole puzzle
        return _move_string

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))


