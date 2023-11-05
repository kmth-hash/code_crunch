#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #house_start = s-a
    #house_end = b-t
    ap = 0
    bp = 0
    for i in apples:
        #print(a+i)
        if a+i>=s and a+i<=t:
            ap+=1
    for i in oranges:
        #print(b+i)
        if b+i>=s and b+i<=t:
            bp+=1
    print(ap)
    print(bp)
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
