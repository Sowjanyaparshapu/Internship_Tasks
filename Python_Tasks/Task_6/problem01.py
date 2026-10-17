# If-Else condition
#problem link - https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python3

import math
import os
import random
import re
import sys
def conditional_program(n):
    if n%2!=0:
        print("Weird")
    elif n%2==0 and n in range(2,6):
        print("Not Weird")
    elif n%2==0 and n in range(6,21):
            print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
        


if __name__ == '__main__':
    n = int(input().strip())
    conditional_program(n)
