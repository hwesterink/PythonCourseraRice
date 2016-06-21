"""
Computing Fabonacci numbers using recursion and memorization of computed numbers
"""
count = 0


def memoized_fib(num, memo_dict):
    global count
    count += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2


for index in range(1,50):
    count = 0
    print index, memoized_fib(index, {0:0, 1:1}), count, 2*index-1
        
