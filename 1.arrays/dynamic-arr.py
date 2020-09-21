import math
import os
import random
import re
import sys


def dynamicArray(n, queries):
    # Write your code here
    last_ans = 0
    a = []
    # arr_result = []

    for i in range(n):
        a.append([])

    for j in queries:
        x,y = j[1], j[2]
        if j[1] == 1:
            sequence = (x ^ last_ans) % n
            a[sequence].append(y)

        elif j[2]  == 2:
            sequence = (x ^ last_ans) % n
            size = y % len(a[sequence])
            vals = a[sequence][size]
            # arr_result.append(last_ans)
            last_ans = vals
            

    return last_ans
    # print(arr_result)
    # print(last_ans)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    dynamicArray(n, queries)
    # result = dynamicArray(n, queries)
    # print(result)