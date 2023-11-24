#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    step = 0
    
    ln = len(c)
    c.append(1)
    c.append(1)
    print(c)
    while step!=ln-1:
        if c[step+2]!=1:
            step = step+2
            count+=1
        else:
            step = step+1
            count = count+1
        print(count,step)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()



