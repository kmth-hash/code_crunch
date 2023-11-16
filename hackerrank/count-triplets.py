#https://www.hackerrank.com/challenges/count-triplets-1/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    s=0
    a = Counter(arr)
    b = Counter()
    for i in arr:
        j = i//r
        k = i*r
        a[i]-=1
        if b[j] and a[k] and not i%r:
            s+=b[j]*a[k]
        b[i]+=1
    return s

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

