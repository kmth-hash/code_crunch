#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
en = int(input())
eng_ls = set(map(int,input().rstrip().split()))

fr = int(input())
fr_ls = set(map(int,input().rstrip().split()))

res = eng_ls.symmetric_difference(fr_ls)

print(len(res))