"""
Student facing code for Tantrix Solitaire
http://www.jaapsch.net/puzzles/tantrix.htm

Game is played on a grid of hexagonal tiles.
All ten tiles for Tantrix Solitaire and place in a corner of the grid.
Click on a tile to rotate it.  Cick and drag to move a tile.

Goal is to position the 10 provided tiles to form
a yellow, red or  blue loop of length 10
"""



# Core modeling idea - a triangular grid of hexagonal tiles are 
# model by integer tuples of the form (h, k, l) 
# where h + k + l == size and h, k, l >= 0.

# Each hexagon has a neighbor in one of six directions
# These directions are modeled by the differences between the 
# tuples of these adjacent tiles

# Numbered directions for hexagonal grid, ordered clockwise at 60 degree intervals
DIRECTIONS = {0 : (-1, 0, 1), 1 : (-1, 1, 0), 2 : (0, 1, -1), 
              3 : (1, 0, -1), 4 : (1, -1, 0), 5 : (0,  -1, 1)}

def reverse_direction(direction):
    """
    Helper function that returns the opposite direction on a hexagonal grid
    """
    num_directions = len(DIRECTIONS)
    return (direction + num_directions / 2) % num_directions



# Color codes for ten tiles in Tantrix Solitaire
# "B" denotes "Blue", "R" denotes "Red", "Y" denotes "Yellow"
SOLITAIRE_CODES = ["BBRRYY", "BBRYYR", "BBYRRY", "BRYBYR", "RBYRYB",
                "YBRYRB", "BBRYRY", "BBYRYR", "YYBRBR", "YYRBRB"]


# Minimal size of grid to allow placement of 10 tiles
MINIMAL_GRID_SIZE = 4



class Tantrix:
    """
    Basic Tantrix game class
    """
    
    def __init__(self, size):
        """
        Create a triangular grid of hexagons with size + 1 tiles on each side.
        """
        assert size >= MINIMAL_GRID_SIZE
        self._tiling_size = size

        # Initialize dictionary tile_value to contain codes for ten
        # tiles in Solitaire Tantrix in one 4x4 corner of grid
        self._tile_value = {}
        _counter = 0        
        for _h in range(MINIMAL_GRID_SIZE):
            for _k in range(MINIMAL_GRID_SIZE - _h):
                _l = size - (_h + _k)
                grid_index = (_h, _k, _l)
                self.place_tile(grid_index, SOLITAIRE_CODES[_counter])
                _counter += 1
                
    def __str__(self):
        """
        Return string of dictionary of tile positions and values
        """
        return str(self._tile_value)
        
    def get_tiling_size(self):
        """
        Return size of board for GUI
        """
        return self._tiling_size
    
    def tile_exists(self, index):
        """
        Return whether a tile with given index exists
        """
        return self._tile_value.has_key(index)
    
    def place_tile(self, index, code):
        """
        Play a tile with code at cell with given index
        """
        self._tile_value[index] = code       

    def remove_tile(self, index):
        """
        Remove a tile at cell with given index
        and return the code value for that tile
        """
        return self._tile_value.pop(index)
               
    def rotate_tile(self, index):
        """
        Rotate a tile clockwise at cell with given index
        """
        _old_string = self._tile_value[index]
        _new_string = _old_string[-1] + _old_string[:-1]
        self._tile_value[index] = _new_string

    def get_code(self, index):
        """
        Return the code of the tile at cell with given index
        """
        return self._tile_value[index]

    def get_neighbor(self, index, direction):
        """
        Return the index of the tile neighboring the tile with given index in given direction
        """
        _neighbor_index = tuple([(index[_dim] + DIRECTIONS[direction][_dim]) for _dim in range(3)])
        return _neighbor_index

    def is_legal(self):
        """
        Check whether a tile configuration obeys color matching rules for adjacent tiles
        """
        # check all tiles
        for tile_index in self._tile_value.keys():
            # check all directions for the selected tile
            for direction in DIRECTIONS.keys():
                neighbor_index = self.get_neighbor(tile_index, direction)
                # check the color for the selected tile and direction
                if self.tile_exists(neighbor_index):
                    if (self._tile_value[tile_index][direction] != 
                        self.get_code(neighbor_index)[reverse_direction(direction)]):
                        # different colors so the configuration is illegal
                        return False
        return True
            
    def has_loop(self, color):
        """
        Check whether a tile configuration has a loop of size 10 of given color
        """
        # check for a legal configuration
        if not self.is_legal():
            return False        
        
        # choose arbitrary starting point and find you way to the next tile
        tile_indices = self._tile_value.keys()
        start_index = tile_indices[0]
        start_code = self._tile_value[start_index]
        next_direction = start_code.find(color)
        next_index = self.get_neighbor(start_index, next_direction)
        current_length = 1
   
        # loop through neighboring tiles that match given color
        while start_index != next_index:
            current_index = next_index
            # if there is no tile for the right color there is no loop
            if not self.tile_exists(current_index):
                return False
            current_code = self._tile_value[current_index]
            # find the next tile
            if current_code.find(color) == reverse_direction(next_direction):
                next_direction = current_code.rfind(color)
            else:
                next_direction = current_code.find(color)
            next_index = self.get_neighbor(current_index, next_direction)
            current_length += 1
      
        return current_length == len(SOLITAIRE_CODES)

    
# run GUI for Tantrix
import poc_tantrix_gui
poc_tantrix_gui.TantrixGUI(Tantrix(6))
