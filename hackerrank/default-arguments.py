#https://www.hackerrank.com/challenges/default-arguments/problem

n = int(input())
for i in range(n):
    x,d = input().split()
    i = 0
    if x=='odd':
        i = 1
    for j in range(int(d)):
        
        print(i)
        i+=2
        