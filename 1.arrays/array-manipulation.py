import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    my_arr = [0] * n

    for q in queries:
        my_arr[q[0] - 1] += q[2]
        if q[1] != len(my_arr):
            my_arr[q[1]] -= q[2]

    max_num = 0
    total_count = 0
    # print(my_arr)

    for x in my_arr:
        total_count += x
        if total_count > max_num:
            max_num = total_count

    # return max_num
    print(max_num)

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    arrayManipulation(n, queries)
    # result = arrayManipulation(n, queries)

"""
Sample input 1
5 3
1 2 100
2 5 100
3 4 100
Sample output 1
200

Sample Input  2
10 4
2 6 8
3 5 7
1 8 1
5 9 15
Sample output 2
31
"""