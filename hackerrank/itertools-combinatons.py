#https://www.hackerrank.com/challenges/itertools-combinations/problem
from itertools import combinations

w , l = input().rstrip().split()
l = int(l)
w = sorted(w)
res = []
for j in range(l):
    
    res.extend([''.join(i) for i in list(combinations(w,j+1))] )
for j in res:
    print(j)