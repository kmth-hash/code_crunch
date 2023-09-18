#https://www.hackerrank.com/challenges/py-set-union/problem

x = input()
e = set(map(int , input().rstrip().split()))
y = input()
f = set(map(int , input().rstrip().split()))
res = e.union(f)
print(len(res))