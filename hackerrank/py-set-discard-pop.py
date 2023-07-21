#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = list(map(int, input().split()))
m = int(input())
ls = []
for i in range(m):
    ls.append(input().split())


for i in ls:
    if i[0]=='pop':
        s = s[1:]
    if i[0]=='discard' or i[0]=='remove':
        if int(i[1]) in s :
            s.remove(int(i[1]))
print(sum(s))