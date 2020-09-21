import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    q_res = []

    for q in queries:
        counter = 0
        for s in strings:
            if str(q) == str(s):
                counter += 1

        # print(counter)
        q_res.append(counter)

    print(q_res) # | return q_res

if __name__ == '__main__':
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    matchingStrings(strings, queries)
    # res = matchingStrings(strings, queries)