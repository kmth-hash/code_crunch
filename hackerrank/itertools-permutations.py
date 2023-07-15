#https://www.hackerrank.com/challenges/itertools-permutations/problem
from itertools import permutations

n = input()
n,m = n.split()
k = [i for i in n if i.isupper()]

p = list(permutations(k,int(m)))
ls = list([i for i in (''.join(i) for i in p)])
ls.sort()
for i in ls :
    print(i)