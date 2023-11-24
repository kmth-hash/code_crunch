#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c = 0
    
    sl = 0
    
    for i in s:
        if i=='D':
            sl = sl-1
            
        else:
            sl=sl+1
            if sl==0:
                c+=1
        
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
