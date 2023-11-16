#https://www.hackerrank.com/challenges/luck-balance/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    ls = []
    tot = 0
    for i in contests:
        if i[1]==1:            
            ls.append(i[0])
        else : 
            tot+=i[0]
    
    ls.sort(reverse = True)
    print(ls , tot)
    return tot + sum(ls[:k]) - sum(ls[k:])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
