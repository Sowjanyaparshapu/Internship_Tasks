# game of thrones
# problem link - https://www.hackerrank.com/challenges/game-of-thrones/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def gameOfThrones(s):
    char_count = Counter(s)
    odd_count = 0

    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
