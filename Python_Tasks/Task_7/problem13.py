# Sherlock and Valid String
# Problem link -  https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    freq = list(freq_count.keys())
    count = list(freq_count.values())

    if (freq[0] == 1 and count[0] == 1):
        return "YES"

    if (freq[1] == 1 and count[1] == 1):
        return "YES"

    if abs(freq[0] - freq[1]) == 1:
        if freq[0] > freq[1] and count[0] == 1:
            return "YES"
        if freq[1] > freq[0] and count[1] == 1:
            return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
