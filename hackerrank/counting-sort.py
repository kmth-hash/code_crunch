#https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    ls = [0]*(100)
    for i in arr:
        ls[i]+=1
    print(max(arr) , ls[-1])
    return ls

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
