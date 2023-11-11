#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    res = []
    for i in range(4):
        for j in range(4):
            print('*'*40)
            tmp = sum(arr[i][j:j+3])
            print(tmp)
            tmp= tmp + arr[i+1][j+1]
            print(tmp)
            tmp = tmp + sum(arr[i+2][j:j+3])
            print(tmp)
            res.append(tmp)
    print(res)
    return max(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
