import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = -1000

    for row in range(len(arr)):
        tempSum = 0
        for col in range(len(arr[row])):
            if col+2 >= len(arr[row]) or row+2 >= len(arr[col]):
                continue
            tempSum = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            if maxSum < tempSum:
                maxSum = tempSum

    # return maxSum
    print(maxSum)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglassSum(arr)