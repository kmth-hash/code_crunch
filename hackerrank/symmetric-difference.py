#https://www.hackerrank.com/challenges/symmetric-difference/problem
n = int(input())
ls = set(map(int , input().rstrip().split()))
m = int(input())
rs = set(map(int , input().rstrip().split()))

res = list((ls.union(rs)).difference(ls.intersection(rs)))
res.sort()
for i in res:
    print(i)