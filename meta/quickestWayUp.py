#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

from collections import deque


def quickestWayUp(ladders, snakes):
    # Write your code here
    paths = {}
    for s, d in ladders + snakes:
        paths[s] = d

    q = deque([(1, 0)])
    visited = set()
    while q:
        sq, rolls = q.popleft()
        if 100 == sq:
            return rolls

        visited.add(sq)
        for i in range(1, 7):
            next = sq + i
            if next in visited or next > 100: continue

            q.append((next in paths and paths[next] or next, rolls + 1))
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
