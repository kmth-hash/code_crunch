#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
B = []
for i in range(n):
    A[input()].append(str(i+1))
for i in range(m):
    B.append(input())

for x in B:
    if x in A:
        l = ' '.join(A[x])
        print(l)
    else:
        print('-1')