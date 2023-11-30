#https://www.hackerrank.com/challenges/frequency-queries/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    ls = []
    res = []
    for i in queries:        
        n,m = i        
        if n==1:
            ls.append(m)            
        elif n==2:
            if m in ls :
                ls.remove(m)
        elif n==3:
            x=0
            for j in ls:
                if ls.count(j)==m:
                    x = 1
                    break
            res.append(x)
        # print('ls',*ls)
    return res
                    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
