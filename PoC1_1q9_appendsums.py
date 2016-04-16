def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements
    of lst to lst. Do this 25 times.
    """
    for num in range(25):
        sum = lst[num] + lst[num+1] + lst[num+2]
        lst.append(sum)

sum_three = [0, 1, 2]
appendsums(sum_three)
print "10 =", sum_three[10]
print "20 =", sum_three[20]