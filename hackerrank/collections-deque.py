#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

from collections import deque

d = deque()

n = int(input())
ls = []
for i in range(n):
    ls.append(input())
    
for i in ls :
    if i.split()[0]=='pop':
        d.pop() 
    elif i.split()[0]=='append':
        d.append(i.split()[1])
    elif i.split()[0]=='appendleft':
        d.appendleft(i.split()[1])
    elif i.split()[0]=='popleft':
        d.popleft()
        
print(*d)
