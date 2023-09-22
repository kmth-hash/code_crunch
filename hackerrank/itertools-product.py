#https://www.hackerrank.com/challenges/itertools-product/problem
import itertools 

a = list(map(int , input().rstrip().split()))
b = list(map(int , input().rstrip().split()))

res = list(itertools.product(a,b))
for i in res : 
    print(i , end =' ')