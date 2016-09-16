"""
Functions developed for project #4:
Computing Alignment of Functions

The following functions were developed:

build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score)
compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag)
compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix)
"""

######################################################
# Imports needed in the functions

# None


######################################################
# Code for the functions that generate the matrices

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Takes as input a set of characters alphabet and three scores diag_score, off_diag_score
    and dash_score. The function returns a dictionary of dictionaries whose entries are
    indexed by pairs of characters in alphabet plus '-'. The score for any entry indexed by
    one or more dashes is dash_score. The score for the remaining diagonal entries is diag_score.
    Finally, he score for the remaining off_diagonal entries is off_diag_score.
    """
    # Initialize variables needed in the function
    _chars = ""
    for _char in alphabet:
        _chars += _char
    _chars += "-"
    _num_chars = len(_chars)
    
    # Initialize the scoring matrix with the off_diag_score
    _scoring_matrix = {}
    for _index1 in range(_num_chars):
        _scoring_matrix_row = {}
        for _index2 in range(_num_chars):
            _scoring_matrix_row [_chars[_index2]] = off_diag_score
        _scoring_matrix [_chars[_index1]] = _scoring_matrix_row

    for _index in range(_num_chars):
        # Replace the entries on the diagonal with the diag_score
        _scoring_matrix [_chars[_index]][_chars[_index]] = diag_score
        # Replace the entries indexed by one or more '-' with the dash_score
        _scoring_matrix [_chars[_index]]["-"] = dash_score
        _scoring_matrix ["-"][_chars[_index]] = dash_score
    
    return _scoring_matrix


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag = True):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with
    the scoring matrix scoring_matrix. The function computes and returns the alignment matrix
    for seq_x and seq_y as described in Homework. If global_flag is True (which is the default),
    each entry of the alignment matrix is computed using the method described in Question 8 of
    Homework. If global_flag is False, each entry is computed using the method described in
    Question 12 of the Homework.
    """
    # Initialize values needed in this function
    _len_x = len(seq_x)
    _len_y = len(seq_y)
    _alignment_matrix = [[0]]

    # Fill the first column of the alignment matrix
    for _index in range(1, _len_x+1):
        if global_flag:
            _new_list = [_alignment_matrix[_index-1][0] +
                        scoring_matrix[seq_x[_index-1]]["-"]]
        else:
            _new_list = [0]
        _alignment_matrix.append(_new_list)
    
    # Fill the first row of the alignment matrix
    for _index in range(1, _len_y+1):
        if global_flag:
            _new_item = ( _alignment_matrix[0][_index-1] +
                        scoring_matrix["-"][seq_y[_index-1]] )
        else:
            _new_item = 0
        _alignment_matrix[0].append(_new_item)

    # Fill the rest of the alignment matrix column by column
    for _index1 in range(1, _len_x+1):
        for _index2 in range(1, _len_y+1):
            _new_item = max( _alignment_matrix[_index1-1][_index2-1] + scoring_matrix[seq_x[_index1-1]][seq_y[_index2-1]],
                             _alignment_matrix[_index1-1][_index2] + scoring_matrix[seq_x[_index1-1]]["-"],
                             _alignment_matrix[_index1][_index2-1] + scoring_matrix["-"][seq_y[_index2-1]] )
            if not(global_flag) and _new_item < 0:
                _new_item = 0
            _alignment_matrix[_index1].append(_new_item)
        if _index1 % 200 == 0:
            print "==========>", _index1, "rows of", _len_x+1, "processed."

    return _alignment_matrix
 
    
######################################################
# Code for the functions that compute the global or local alignments

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. This function computes a global alignment of 
    seq_x and seq_y using the global alignment matrix alignment_matrix. The function returns
    a tuple of the form (score, align_x, align_y) where score is the score of the global
    alignment align_x and align_y. Note that align_x and align_y should have the same length
    and may include the padding character '-'.
    """

    # Initialize variables needed in this function
    _pos_x = len(seq_x)
    _pos_y = len(seq_y)
    _align_x = ""
    _align_y = ""
    
    # Determine score
    _score = alignment_matrix[_pos_x][_pos_y]
    
    # Create align_x and align_y
    while ( _pos_x != 0 ) and ( _pos_y != 0 ):
        if ( alignment_matrix[_pos_x][_pos_y] ) == ( alignment_matrix[_pos_x-1][_pos_y-1] +
                                                     scoring_matrix[seq_x[_pos_x-1]][seq_y[_pos_y-1]] ):
            _align_x = seq_x[_pos_x-1] + _align_x
            _align_y = seq_y[_pos_y-1] + _align_y
            _pos_x -= 1
            _pos_y -= 1
        else:
            if ( alignment_matrix[_pos_x][_pos_y] ) == ( alignment_matrix[_pos_x-1][_pos_y] +
                                                       scoring_matrix[seq_x[_pos_x-1]]["-"] ):
                _align_x = seq_x[_pos_x-1] + _align_x
                _align_y = "-" + _align_y
                _pos_x -= 1
            else:
                _align_x = "-" + _align_x
                _align_y = seq_y[_pos_y-1] + _align_y
                _pos_y -= 1

    while _pos_x != 0:
        _align_x = seq_x[_pos_x-1] + _align_x
        _align_y = "-" + _align_y
        _pos_x -= 1

    while _pos_y != 0:
        _align_x = "-" + _align_x
        _align_y = seq_y[_pos_y-1] + _align_y
        _pos_y -= 1

    return ( _score, _align_x, _align_y )


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix scoring_matrix. This function computes a local alignment of 
    seq_x and seq_y using the local alignment matrix alignment_matrix. The function returns
    a tuple of the form (score, align_x, align_y) where score is the score of the optimal local
    alignment align_x and align_y. Note that align_x and align_y should have the same length
    and may include the padding character '-'.
    """

    # Initialize variables needed for this function
    _align_x = ""
    _align_y = ""
    _score = 0
    _maximum = -1
    _pos_x = -1
    _pos_y = -1
    _len_col = len(alignment_matrix[0])

    # Determine starting position and score
    for _index1 in range(len(alignment_matrix)):
        for _index2 in range(_len_col):
            if alignment_matrix[_index1][_index2] >= _maximum:
                _maximum = alignment_matrix[_index1][_index2]
                _pos_x = _index1
                _pos_y = _index2
    
    # Create align_x and align_y
    while alignment_matrix[_pos_x][_pos_y] > 0:
        if ( alignment_matrix[_pos_x][_pos_y] ) == ( alignment_matrix[_pos_x-1][_pos_y-1] +
                                                     scoring_matrix[seq_x[_pos_x-1]][seq_y[_pos_y-1]] ):
            _align_x = seq_x[_pos_x-1] + _align_x
            _align_y = seq_y[_pos_y-1] + _align_y
            _pos_x -= 1
            _pos_y -= 1
        else:
            if ( alignment_matrix[_pos_x][_pos_y] ) == ( alignment_matrix[_pos_x-1][_pos_y] +
                                                       scoring_matrix[seq_x[_pos_x-1]]["-"] ):
                _align_x = seq_x[_pos_x-1] + _align_x
                _align_y = "-" + _align_y
                _pos_x -= 1
            else:
                _align_x = "-" + _align_x
                _align_y = seq_y[_pos_y-1] + _align_y
                _pos_y -= 1
            
    # Compute score for the local alignment
    for _index in range(len(_align_x)):
        _score += scoring_matrix[_align_x[_index]][_align_y[_index]]

    return (_score, _align_x, _align_y)
