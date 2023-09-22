#https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem?

import math
import os
import random
import re
import sys

def timeConversion(s):
    if 'PM' in s :
        h,r = int(s[:2]) , s[2:-2]
        if h!=12:
            return f"{h+12:02}{r}"
        else:
            return f"{h:02}{r}"
    if 'AM' in s :
        h,r = int(s[:2]) , s[2:-2]
        if h==12:
            return f'00{r}'
        return f'{h:02}{r}'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
