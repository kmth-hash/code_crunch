#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
#Method 1

# for i in range(int(input())):
#     _ = input()
#     ls = list(map(int , input().rstrip().split()))
#     _ = input()
#     rs = list(map(int , input().rstrip().split()))
    
#     f = True
#     for j in ls:
#         if j not in rs:
#             f = False 
#             break 
#     print(f)           

# Method 2 

ls = set(map(int , input().rstrip().split()))

n = int(input())

rs = set()

for i in range(n):
    x = set(map(int , input().rstrip().split()))
    rs = rs.union(x)
    # print(x)
l1 = len(ls)
ls = ls.union(rs)
l2 = len(ls)

if l2>l1:
    print(False)
else:
    print(True)
