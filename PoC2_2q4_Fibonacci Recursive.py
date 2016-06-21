"""
Compute Fabonacci numbers using recursion
"""
count = 0
countold = 0


def fib(num):
    global count
    count += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


for index in range(20):
    countoldold = countold
    countold = count
    count = 0
    print index, fib(index), count, countold, countoldold, countold+countoldold+1
