#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter 

n = int(input())

ls = list(map(int , input().split()))
    
m = int(input())

amt = 0
for i in range(m):
    rs = list(map(int , input().split()))
    # print(rs,amt,ls)
    if rs[0] in ls :
        amt += rs[1]
        ls.remove(rs[0])
print(amt)
