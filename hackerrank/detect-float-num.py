#https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re
def findIt(n):
    x = re.compile('^[+-]?[0-9]*\.[0-9]+$')
    
    if x.match(n):
        return True
    else:
        return False
        
for i in range(int(input())):
    print(findIt(input()))

