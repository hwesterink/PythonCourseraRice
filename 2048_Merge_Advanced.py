"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # move all the empty tiles to the end of the line
    line = move_empty(line)
    # merge adjacent tiles with equal value
    for num in range(len(line)-1):
        if line[num] == line[num+1]:
            line[num] *= 2
            line[num+1] = 0
    # move all the empty tiles to the end of the line
    line = move_empty(line)
    return line

def move_empty(line):
    """
    Function that moves all empty tiles to the end of the list.
    """
    new_line = []
    count_zero = 0
    for num in range(len(line)):
        if line[num] == 0:
            count_zero += 1
        else:
            new_line.append(line[num])
    # vul aan met nullen
    for num in range(count_zero):
        new_line.append(0)
    return new_line

def merge2(line):  
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
            elif merged | (new_line[-1] != line[num]):
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
    
# Test to do intermediate tests on code
def run_test():
    """
    Function that runs tests for merge/merge2
    """
#    my_list = [0, 2, 0, 2, 4, 0, 0, 8]
#    my_list = [2, 2, 4, 8]
#    my_list = []
    my_list = [2, 0, 2, 4]
    print "my_list before merge =", my_list
    print "returned by merge    =", merge2(my_list), "expected [4, 4, 0, 0]"
    my_list = [0, 0, 2, 2]
    print "my_list before merge =", my_list
    print "returned by merge    =", merge2(my_list), "expected [4, 0, 0, 0]"
    my_list = [2, 2, 0, 0]
    print "my_list before merge =", my_list
    print "returned by merge    =", merge2(my_list), "expected [4, 0, 0, 0]"
    my_list = [2, 2, 2, 2, 2]
    print "my_list before merge =", my_list
    print "returned by merge    =", merge2(my_list), "expected [4, 4, 2, 0, 0]"
    my_list = [8, 16, 16, 8]
    print "my_list before merge =", my_list
    print "returned by merge    =", merge2(my_list), "expected [8, 32, 8, 0]"
    
run_test()