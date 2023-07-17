#https://www.hackerrank.com/challenges/compress-the-string/problem
s = [int(i) for i in input()]
ls = [[1,s[0]]]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        rs = ls[-1]
        rs[0]+=1
        ls[-1] = rs
        
    else:
        rs = [1,s[i]]
        ls.append(rs)
        

for i in ls:
    print(f'({i[0]}, {i[1]})',end=' ')
        
        
