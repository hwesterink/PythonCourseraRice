"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function plays a game of Tic-Tac-Toe starting with the input
    board and the input player to start with. The function stops when
    the game is completed and modifies the board while playing. 
    """
    # Find empty cells
    _list_empty_cells = board.get_empty_squares()
    # For every empty cell
    _initial_lenght = len(_list_empty_cells)
    for _dummy_index in range(_initial_lenght):
        ## Select a random cell to assign and assign it
        _selected_cell = random.randrange(len(_list_empty_cells))
        board.move(_list_empty_cells[_selected_cell][0],
                   _list_empty_cells[_selected_cell][1], player)
        ## Detect whether the game has ended and return when ready
        if board.check_win() != None:
            return
        ## Update empty cells by removing the selected cell
        _list_empty_cells.pop(_selected_cell)
        ## Switch player
        player = provided.switch_player(player)
    return

def mc_update_scores(scores, board, player):
    """
    This function updates the scores grid based on the completed board
    received as input. The player given in the input is the machine
    player.
    """
    _game_dim = board.get_dim()
    _other_player = provided.switch_player(player)
    # Define the winner on the board
    _game_result = board.check_win()
    # Update the scores depending on the winner
    if _game_result == player:
        ## The machine player is the winner, the scores are changed accordingly
        for _row in range(_game_dim):
            for _col in range(_game_dim):
                if board.square(_row, _col) == provided.EMPTY:
                    pass
                elif board.square(_row, _col) == player:
                    scores[_row][_col] += SCORE_CURRENT
                else:
                    scores[_row][_col] -= SCORE_OTHER
    elif _game_result == _other_player:
        ## The human player is the winner, the scores are changed accordingly
        for _row in range(_game_dim):
            for _col in range(_game_dim):
                if board.square(_row, _col) == provided.EMPTY:
                    pass
                elif board.square(_row, _col) == player:
                    scores[_row][_col] -= SCORE_CURRENT
                else:
                    scores[_row][_col] += SCORE_OTHER
    return

def get_best_move(board, scores):
    """
    This function selects the best next move based on the computed
    scores grid in the input and returns it as a (row,column) tuple.
    In case there are multiple empty cells with the highest score,
    one of them is randomly selected and returned. If the board is
    full already, the function returns None.
    """
    _max_score = None
    _game_dim = board.get_dim()
    # Find the empty cells with the maximum score in the scores grid and create
    # a list of them.
    _empty_squares = board.get_empty_squares()
    for _row, _col in _empty_squares:
        if (_max_score < scores[_row][_col]) or (_max_score == None):
            _max_list = [(_row,_col)]
            _max_score = scores[_row][_col]
        elif _max_score == scores[_row][_col]:
            _max_list.append((_row,_col))
    # Select one of the cells with a maximum score as _best_move.
    _selection = random.randrange(len(_max_list))
    return _max_list[_selection]

def mc_move(board, player, trials):
    """
    This function returns the best move as a (row,column) tuple on the
    input board for the machine player in the input, based on a Monte
    Carlo Simulation over the number of trails in the input.
    """
    # Create an empty scores grid.
    _game_dim = board.get_dim()
    _scores = [ [0 for _dummy_col in range(_game_dim)]
                 for _dummy_row in range(_game_dim)]
    _init_player = player
    # Play trail-games and build a scores grid.
    for _dummy_trial in range(trials):
        ## Create a copy of the current board to play the trail on.
        _trial_board = board.clone()
        ## Play a trail-game.
        mc_trial(_trial_board, player)
        ## Update the scores grid.
        mc_update_scores(_scores, _trial_board, _init_player)
    # Select the move with the best score. 
    _move = get_best_move(board, _scores)
    return _move


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer. Both should be commented out when you submit 
# for testing to save time.
#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
