#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
for i in range(int(input())):
    _ = input()
    ls = list(map(int , input().rstrip().split()))
    _ = input()
    rs = list(map(int , input().rstrip().split()))
    
    f = True
    for j in ls:
        if j not in rs:
            f = False 
            break 
    print(f)           
    