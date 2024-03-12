#https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem?

#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
    # Write your code here 
    x = 0        
    x = sum([int(i) for i in n])    
    x = x*k
    x = str(x)
    if len(x) == 1:
        return x
    else:
        return superDigit(x, 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
