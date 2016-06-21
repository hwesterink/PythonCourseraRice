'''
Practice Activity 2.1: Recursion
'''
def triangular_sum(num):
    # Assignment 1 of practice activity 2.1
    if num == 0:
        return 0
    else:
        return num + triangular_sum(num-1)

def number_of_threes(num):
    # Assignment 2 of practice activity 2.1
    if num == 0:
        return 0
    else:
        if (num % 10) == 3:
            return 1 + number_of_threes(num//10)
        else:
            return number_of_threes(num//10)

def is_member(my_list, elem):
    # Assignment 3 of practice activity 2.1
    if len(my_list) == 0:
        return False
    else:
        if my_list[0] == elem:
            return True
        else:
            return is_member(my_list[1:],elem)

def remove_x(my_string):
    # Assignment 4 of practice activity 2.1
    if len(my_string) == 0:
        return ""
    else:
        if my_string[0] == "x" or my_string[0] == "X":
            return remove_x(my_string[1:])
        else:
            return my_string[0] + remove_x(my_string[1:])

def insert_x(my_string):
    # Assignment 5 of practice activity 2.1
    if len(my_string) == 1:
        return my_string
    else:
        return my_string[0] + "x" + insert_x(my_string[1:])

def list_reverse(my_list):
    # Assignment 6 of practice activity 2.1
    if len(my_list) == 1:
        return my_list
    else:
        return list_reverse(my_list[1:]) + my_list[0:1]    

def gcd(num1, num2):
    # Assignment 7 of practice activity 2.1
    if num2 > num1:
        num1, num2 = num2, num1
    if num2 == 0:
        return num1
    else:
        return gcd(num1-num2,num2)

def slice(my_list, first, last):
    # Assignment 8 of practice activity 2.1
    if first == 0 and last == len(my_list):
        return my_list
    elif first == 0:
        my_list.pop(last)
        return slice(my_list, first, last)
    else:
        my_list.pop(0)
        return slice(my_list, first-1, last-1)
    

# Tests for the functions written above

print "Testing triangular_sum: Expected: 6; Computed:", triangular_sum(3)
print "Testing number_of_threes: Expected: 2; Computed:", number_of_threes(34534)
print "Testing is_member: Expected: True; Computed:", is_member(['c', 'a', 't'], 'a')
print "Testing remove_x: Expected: catdog; Computed:", remove_x("catxxdogx")
print "Testing insert_x: Expected: cxaxtxdxoxg; Computed:", insert_x("catdog")
print "Testing list_reverse: Expected: [1, 3, 2]; Computed:", list_reverse([2, 3, 1])
print "Testing gcd: Expected: 5; Computed:", gcd(25,105)
print "Testing slice: Expected: ['c', 'd']; Computed:", slice(['a', 'b', 'c', 'd', 'e'], 2, 4)
