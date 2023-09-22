#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement

w , l = input().rstrip().split()
l = int(l)
w = sorted(w)
res = []

res=list([''.join(i) for i in list(combinations_with_replacement(w,l))] )
for j in res:
    print(j)