#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    d = dict()
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    # print(d)
    for i in b:
        if i not in d:
            d[i]=-1
        else:
            d[i]-=1
    res = 0;
    # print(d)
    for k,v in d.items():
        if v<0:
            res+=(v*-1)
        elif v>0:
            res+=v
    print(res)
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
