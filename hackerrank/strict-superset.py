#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
ls = list(map(int , input().rstrip().split()))

n = int(input())

rs = []
for i in range(n):
    rs.extend(list(map(int , input().rstrip().split())))
flag = 0
for i in rs:
    if i not in ls:
        flag = 1
        break
if flag==1:
    print(False)
else:
    print(True)
    

