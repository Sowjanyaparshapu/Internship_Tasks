# Anagram
# problem link - https://www.hackerrank.com/challenges/anagram/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    s = s.strip()
    n = len(s)
    if n % 2 == 1:
        return -1
    c1 = Counter(s[:n // 2])
    c2 = Counter(s[n // 2:])
    changes = 0
    for ch in c1:
        if c1[ch] > c2[ch]:
            changes += c1[ch] - c2[ch]
    return changes




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
