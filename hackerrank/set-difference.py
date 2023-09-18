#https://www.hackerrank.com/challenges/py-set-difference-operation
x=input()
e = set(map(int , input().rstrip().split()))
y = input()
f = set(map(int , input().rstrip().split()))
res = e.difference(f)
print(len(res))