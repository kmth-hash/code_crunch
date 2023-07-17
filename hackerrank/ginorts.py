#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
l = []
u = []
od = []
ed = []
s = input()
for i in s :
    if i.islower():
        l.append(i)
    elif i.isupper():
        u.append(i)
    elif i.isdigit():
        if int(i)%2==0:
            ed.append(i)
        else:
            od.append(i)
l.sort()
u.sort()
od.sort()
ed.sort()
print(''.join(l),''.join(u),''.join(od),''.join(ed),end='',sep='')