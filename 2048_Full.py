"""
My own version of the 2048 game.
"""

import poc_2048_gui
#import poc_simpletest
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Advanced function to merge a single row or column in 2048.
    """
    # Initialize variables for this function
    new_line = []
    merged = False
    # Copy and merge existing numbers to new_line
    for num in range(len(line)):
        if line[num] != 0:
            if len(new_line) == 0:
                new_line.append(line[num])
            elif merged or (new_line[-1] != line[num]):
                new_line.append(line[num])
                merged = False
            else:
                new_line[-1] *= 2
                merged = True
    # Make new_line the same length of line by adding zeroes.
    count_zeroes = len(line) - len(new_line)
    for num in range(count_zeroes):
        new_line.append(0)
    return new_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Init method that creates an object of the TwentyFortyEight Class
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        # Create an empty grid and add two tiles
        self.reset()
        # Create a dictionary with the starting tiles for the merge function
        self._start_dic = {}
        _directions = (UP, DOWN, LEFT, RIGHT)
        for _direction in _directions:
            _starting_points = []
            if _direction == UP:
                for num in range(self._grid_width):
                    _starting_points.append([0, num])
            elif _direction == DOWN:
                for num in range(self._grid_width):
                    _starting_points.append([self._grid_height-1, num])
            elif _direction == LEFT:
                for num in range(self._grid_height):
                    _starting_points.append([num, 0])
            elif _direction == RIGHT:
                for num in range(self._grid_height):
                    _starting_points.append([num, self._grid_width-1])
            self._start_dic[_direction] = _starting_points

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._grid_width)]
                      for dummy_row in range(self._grid_height)]
        # Create two tiles in the initial grid
        self.new_tile()
        self.new_tile()
            
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        _out = ""
        for row in range(self._grid_height):
            _out = _out + str(self._cells[row]) + "\n"
        return _out

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # Select the number of items in the list
        if direction == UP or direction == DOWN:
            _range_count = self._grid_height
        else:
            _range_count = self._grid_width
        _moved = False
        # Merge each column or row in the right direction
        for _start_point in self._start_dic[direction]:
            # Make a list of values to be merged
            _temp_list = []
            _select_point = list(_start_point)
            for dummy_num in range(_range_count):
                _temp_list.append(self._cells[_select_point[0]][_select_point[1]])
                _select_point[0] += OFFSETS[direction][0]
                _select_point[1] += OFFSETS[direction][1]
            # Merge the selected _temp_list
            _temp_list = merge(_temp_list)
            # Return the list into self.cells
            _select_point = list(_start_point)
            for _num in range(_range_count):
                if (self._cells[_select_point[0]][_select_point[1]]
                              != _temp_list[_num]):
                    _moved = True
                self._cells[_select_point[0]][_select_point[1]] = _temp_list[_num]
                _select_point[0] += OFFSETS[direction][0]
                _select_point[1] += OFFSETS[direction][1]
        if _moved:
            # Create new tile in the initial grid if something moved
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Search for empty squares and make a list of them
        _empty_squares = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == 0:
                    _empty_squares.append((row,col))
        # Select a square to transform into a tile
        _selected_square = random.randrange(0, len(_empty_squares))
        # Give the selected square a value
        _value_base = random.randrange(0, 10)
        if _value_base == 9:
            self._cells[_empty_squares[_selected_square][0]][_empty_squares[_selected_square][1]] = 4
        else:
            self._cells[_empty_squares[_selected_square][0]][_empty_squares[_selected_square][1]] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


# Call the GUI to run the game
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

# Call the testsuite developed to test the game
#import user41_yl7yDYeJVe_23 as poc_2048_testsuite
#poc_2048_testsuite.run_suite(TwentyFortyEight)    