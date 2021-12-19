#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    memo = {}

    for index, value in enumerate(arr):
        if m - value in memo:
            return memo[m - value] + 1, index + 1
        elif value not in memo:
            memo[value] = index


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input().strip())

    for t_itr in xrange(t):
        m = int(raw_input().strip())

        n = int(raw_input().strip())

        arr = map(int, raw_input().rstrip().split())

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
