#https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def rm(i,arr):
    arr.remove(i)
    return arr
def sockMerchant(n, ar):
    count = 0
    le_list = set(ar)
    for i in le_list:
        count+= int(ar.count(i)/2)
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
