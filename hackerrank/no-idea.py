#https://www.hackerrank.com/challenges/no-idea/problem
n,m = input().split()
arr = list([int(i) for i in input().split() ])
yep = set([int(i) for i in input().split() ])
nope = set([int(i) for i in input().split() ])
res = 0
res = sum([(i in yep) -(i in nope) for i in arr ])
print(res)
