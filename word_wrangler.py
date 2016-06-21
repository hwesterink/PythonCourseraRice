"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    if ( len(list1) == 0 ) or ( len(list1) == 1 ):
        return list1
    else:
        if list1[0] == list1[1]:
            return remove_duplicates(list1[1:])
        else:
            return list1[0:1] + remove_duplicates(list1[1:])

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    if ( len(list1) == 0 ) or ( len(list2) == 0 ):
        return []
    else:
        if list1[0] == list2[0]:
            return list1[0:1] + intersect(list1[1:], list2[1:])
        elif list1[0] < list2[0]:
            return intersect(list1[1:], list2)
        else:
            return intersect(list1, list2[1:])

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """   
    _list1 = list(list1)
    _list2 = list(list2)
    _result = []
    while ( len(_list1) > 0 ) or ( len(_list2) > 0 ):
        if len(_list1) == 0:
            _result.append(_list2.pop(0))
        elif len(_list2) == 0:
            _result.append(_list1.pop(0))
        elif _list1[0] <= _list2[0]:
            _result.append(_list1.pop(0))
        else:
            _result.append(_list2.pop(0))
    return _result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    _lenght = len(list1)
    if ( _lenght == 0 ) or ( _lenght == 1 ):
        return list1
    else:	
        return merge(merge_sort(list1[0:_lenght//2]), merge_sort(list1[_lenght//2:]))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    if len(word) == 0:
        return [""]
    else:
        _first = word[0]
        _rest_strings = gen_all_strings(word[1:])
        _result = []
        for _rest_string in _rest_strings:
            for _index in range(len(_rest_string)):
                _result.append(_rest_string[0:_index] + _first+ _rest_string[_index:])
            _result.append(_rest_string + _first)
        return _rest_strings + _result

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    _url = codeskulptor.file2url(filename)
    _netfile = urllib2.urlopen(_url)
    
    _data = _netfile.read()
    _words = _data.split("\n")
    
    return _words

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    