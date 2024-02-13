# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    w = (4*size)-3
    a = string.ascii_lowercase

    for i in list(range(size))[::-1]+list(range(1,size)):
        print('-'.join(a[size-1:i:-1]+a[i:size]).center(w,'-'))
