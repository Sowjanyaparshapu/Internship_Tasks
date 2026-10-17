# capitalize
# program link - https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    #return s.title()
    #we can use title(), but all test cases not passing
    

    result = ""
    capitalize_next = True

    for ch in s:
        if ch == " ":
            result += ch
            capitalize_next = True
        elif capitalize_next:
            result += ch.upper()
            capitalize_next = False
        else:
            result += ch

    return result



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
