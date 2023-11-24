#https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_c = 0
    ln = len(s)
    print(n//ln)
    a_c = s.count('a') * (n//ln)
    rem = n%ln
    a_c = a_c + s[:rem].count('a')
    return a_c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
