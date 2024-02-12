# https://www.hackerrank.com/challenges/magic-square-forming/problem


import math
import os
import random
import re
import sys
from itertools import *

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    le_list = [[8,3,4,1,5,9,6,7,2],
    [6,1,8,7,5,3,2,9,4],
    [2,7,6,9,5,1,4,3,8],
    [4,9,2,3,5,7,8,1,6],
    [4,3,8,9,5,1,2,7,6],
    [8,1,6,3,5,7,4,9,2],
    [6,7,2,1,5,9,8,3,4],
    [2,9,4,7,5,3,6,1,8]]
    abs_val = []
    val = []
    for i in s:
        for j in i:
            val.append(j)
    
    for i in le_list:
        tmp = 0
        for itr in range(9) :
            tmp+= (abs(i[itr]-val[itr]))
        abs_val.append(tmp)
    return (min(abs_val))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
