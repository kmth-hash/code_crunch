#https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    ld = 0
    for i in range(len(arr)):
        ld += arr[i][i]
    
    rd = 0
    rdl = 0
    rdr = len(arr)-1
    for i in range(len(arr)):
        rd += arr[rdl][rdr]
        rdl+=1
        rdr-=1
    return(abs(rd-ld))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
