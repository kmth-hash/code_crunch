#https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    mn = 10**9
    #return min([arr[x+k-1]-arr[x] for x in range(len(arr)-k+1)])
    print(arr)
    for i in range(0,len(arr)-k+1):
        mn = min(mn , arr[i+k-1]-arr[i])
    return mn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
