#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

a =int(input())
ls = set(map(int,input().split()))
n = int(input())
for i in range(n):
    b = input().split()
    for j in range(n):
        rs = set(map(int,input().split(' ',int(b[1]))))
        if b[0] == 'update':
            ls.update(rs)
        elif b[0] == 'intersection_update':
            ls.intersection_update(rs)
        elif b[0] == 'difference_update':
            ls.difference_update(rs)
        elif b[0] == 'symmetric_difference_update':
            ls.symmetric_difference_update(rs)
        break
print(sum(ls))