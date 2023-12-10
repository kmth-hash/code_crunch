#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
x = input().split(' ')
k = int(x[0])
m = int(x[1])
le_list = []
for i in range(k):
    tmp = list(map(int,input().rstrip().split(' ')))
    le_list.append(tmp)
for i in range(len(le_list)):
    le_list[i] = le_list[i][1:]
res = []
val = [p for p in itertools.product(*le_list)]
for i in val:
    tmp = 0
    for j in i:
        tmp = tmp + (j**2)
        
    #print(tmp,tmp%m)
    res.append(tmp%m)
#print(sorted(res))
print(max(res))
