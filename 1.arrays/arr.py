import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    a.reverse()
    return a

if __name__ == '__main__':

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    reverseArray(arr)
    # res = reverseArray(arr)

"""
    Sample input
    4
    1 4 3 2
    
    Sample output
    2 3 4 1
"""