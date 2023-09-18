#https://www.hackerrank.com/challenges/py-set-intersection-operation
x = input()
e = set(map(int , input().rstrip().split()))
y = input()
f = set(map(int , input().rstrip().split()))
res = e.intersection(f)
print(len(res))