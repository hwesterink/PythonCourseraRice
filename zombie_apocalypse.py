"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """
    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for _zombie in self._zombie_list:
            yield _zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for _human in self._human_list:
            yield _human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        # Create the second grid named visited
        _visited = poc_grid.Grid(self._grid_height, self._grid_width)
        
        # Create the 2D list distance_field
        _distance_field = [[(self._grid_width * self._grid_height)
                       for _dummy_col in range(self._grid_width)]
                       for _dummy_row in range(self._grid_height)]
        
        # Create the queue boundery
        _boundery = poc_queue.Queue()
        if entity_type == HUMAN:
            _num_humans = len(self._human_list)
            for _index in range(_num_humans):
                _boundery.enqueue(self._human_list[_index])
        else:
            _num_zombies = len(self._zombie_list)
            for _index in range(_num_zombies):
                _boundery.enqueue(self._zombie_list[_index])
        # Process the boundery queue into the visited grid and the
        # distance_field list
        for _entity in _boundery:
            _visited.set_full(_entity[0], _entity[1])
            _distance_field[_entity[0]][_entity[1]] = 0
        
        # Execute the modified Breadth First Search method to fill
        # the 2D distance_field
        while len(_boundery) != 0:
            # Get the next item from the queue
            _current_cell = _boundery.dequeue()
            # Determine neighbor cells
            _neighbor_cells = _visited.four_neighbors(_current_cell[0],_current_cell[1])
            # Process neighbor cells
            for _cell in _neighbor_cells:
                if (_visited.is_empty(_cell[0], _cell[1]) and
                    self.is_empty(_cell[0], _cell[1])):
                    _visited.set_full(_cell[0], _cell[1])
                    _distance_field[_cell[0]][_cell[1]] =  \
                            _distance_field[_current_cell[0]][_current_cell[1]] + 1
                    _boundery.enqueue(_cell)
        
        return _distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        # Move the humans one by one
        _new_human_list = []
        for _human in self._human_list:
            _max_distance = zombie_distance_field[_human[0]][_human[1]]
            _new_human = _human
            # Determine the cells the human can flee to
            _possible_cells = self.eight_neighbors(_human[0],_human[1])
            for _possible_cell in _possible_cells:
                # Flee to the best possible cells
                if self.is_empty(_possible_cell[0],_possible_cell[1]):
                    if (_max_distance < zombie_distance_field[_possible_cell[0]][_possible_cell[1]] or
                        (_max_distance == zombie_distance_field[_possible_cell[0]][_possible_cell[1]] and
                         random.randrange(0, 2) == 1)):
                        _max_distance = zombie_distance_field[_possible_cell[0]][_possible_cell[1]]
                        _new_human = (_possible_cell[0], _possible_cell[1])
            _new_human_list.append(_new_human)
        self._human_list = _new_human_list
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        # Move the zombies one by one
        _new_zombie_list = []
        for _zombie in self._zombie_list:
            _min_distance = human_distance_field[_zombie[0]][_zombie[1]]
            _new_zombie = _zombie
            # Determine the cells the zombie can move to
            _possible_cells = self.four_neighbors(_zombie[0],_zombie[1])
            for _possible_cell in _possible_cells:
                # Move to the best possible cells, closest to a human
                if self.is_empty(_possible_cell[0],_possible_cell[1]):
                    if (_min_distance > human_distance_field[_possible_cell[0]][_possible_cell[1]] or
                        (_min_distance == human_distance_field[_possible_cell[0]][_possible_cell[1]] and
                         random.randrange(0, 2) == 1)):
                        _min_distance = human_distance_field[_possible_cell[0]][_possible_cell[1]]
                        _new_zombie = (_possible_cell[0], _possible_cell[1])
            _new_zombie_list.append(_new_zombie)
        self._zombie_list = _new_zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

#poc_zombie_gui.run_gui(Apocalypse(30, 40))
