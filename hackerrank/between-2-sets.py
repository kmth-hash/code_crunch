#https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Write your code here
    #print(a,b,min(b))
    mn = min(b)
    d = []
    res = 0
    for i in range(max(a),mn+1):
        c = 0
        for j in a:
            if i%j==0:
                c+=1
        if c==len(a):
            d.append(i)
    for i in d:
        c = 0
        for j in b:
            if j%i==0:
                c+=1
        if c==len(b):
            res +=1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
