#https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
from math import floor
def dayN(tot,x,n):
    if n==0:
        print('returning',tot)
        return tot 
    
    res =dayN(tot+floor(x/2),floor(x/2)*3,n-1)
    return res
    
def viralAdvertising(n):
    # Write your code here
    x = dayN(0,5,n)
    
    return(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
