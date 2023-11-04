#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    ls = ''.join([i.upper() if i.islower() else i.lower() for i in s ])
    # print(ls)
    return ls

