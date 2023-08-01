#https://www.hackerrank.com/challenges/word-order/problem
n = int(input())
le_list = []
d = {}
for i in range(n):
    w = input()
    if w in d:
        d[w]+=1
    else:
        d[w] = 1
        le_list.append(w)
print(len(d))
for i in le_list:
    print(d[i],end= ' ')
