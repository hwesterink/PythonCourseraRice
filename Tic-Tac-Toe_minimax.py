"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(120)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # Determine whether the board is already completed
    _next_move = (-1, -1)
    _game_completed = board.check_win()
    if _game_completed == provided.PLAYERO:
        return SCORES[provided.PLAYERO], _next_move
    elif _game_completed == provided.PLAYERX:
        return SCORES[provided.PLAYERX], _next_move
    elif _game_completed == provided.DRAW:
        return SCORES[provided.DRAW], _next_move
    
    # Determine the empty squares on the board
    _empty_squares = board.get_empty_squares()
    
    # Find the best move for the current board
    _max_score = -1
    for _empty_square in _empty_squares:
        _board_copy = board.clone()
        # Add a move to the board on the current square
        _board_copy.move(_empty_square[0], _empty_square[1], player)
        # Change player and find score and move of the next board
        _new_player = provided.switch_player(player)
        _new_score, _dummy_new_square = mm_move(_board_copy, _new_player)
        _check_score = _new_score * SCORES[player]
        if _check_score == 1:
            # Ready, you have reached the best possible score
            return SCORES[player], _empty_square
        elif _check_score == 0 and _max_score == -1:
            # Save the new _max_score and the _next_move to return and
            # search on for a better move
            _max_score = 0
            _next_move = _empty_square
        elif _check_score == -1 and _max_score == -1:
            # Save the _next_move to return and search for a better move
            _next_move = _empty_square
        
    # Return the best possible move for the player
    return _max_score * SCORES[player], _next_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
