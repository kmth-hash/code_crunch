#https://www.hackerrank.com/challenges/ctci-ransom-note/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys



def checkMagazine(magazine, note):
    
    if len(note) > len(magazine):
        print('No')
    flag = 'Yes'
    for i in note:
        if note.count(i) > magazine.count(i):
            flag = 'No'
            break
    print(flag)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
