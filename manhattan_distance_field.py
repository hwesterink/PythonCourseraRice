"""
An example of creating a distance field using Manhattan distance
"""

import math

GRID_HEIGHT = 6
GRID_WIDTH = 8


def manhattan_distance(row0, col0, row1, col1):
    """
    Compute the Manhattan distance between the cells
    (row0, col0) and (row1, col1)
    """
    return int(math.fabs(row0 - row1)) + int(math.fabs(col0 - col1))
        

def create_distance_field(entity_list):
    """
    Create a Manhattan distance field that contains the minimum distance to 
    each entity (zombies or humans) in entity_list
    Each entity is represented as a grid position of the form (row, col) 
    """
    # Initialize an empty distance field
    _distance_field = [[0 for _dummy_col in range(GRID_WIDTH)]
                       for _dummy_row in range(GRID_HEIGHT)]
    
    # Compute the minimal distances from every field in the grid to the items
    for _row in range(GRID_HEIGHT):
        for _col in range(GRID_WIDTH):
            _distance = min([manhattan_distance(entity[0], entity[1], _row, _col)
                                for entity in entity_list])
            _distance_field[_row][_col] = _distance
    return _distance_field
        
    
def print_field(field):
    """
    Print a distance field in a human readable manner with 
    one row per line
    """
    for _distance_row in field:
        print _distance_row

def run_example():
    """
    Create and print a small distance field
    """
    field = create_distance_field([[4, 0],[2, 5]])
    print_field(field)
    
run_example()


# Sample output for the default example
#[4, 5, 5, 4, 3, 2, 3, 4]
#[3, 4, 4, 3, 2, 1, 2, 3]
#[2, 3, 3, 2, 1, 0, 1, 2]
#[1, 2, 3, 3, 2, 1, 2, 3]
#[0, 1, 2, 3, 3, 2, 3, 4]
#[1, 2, 3, 4, 4, 3, 4, 5]
    
    
