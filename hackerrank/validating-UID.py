// https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true

for _ in range(int(input())):
    ls = {'upper' : 0 , 'digit' : 0 , 'notalpha' : 0 }
    res = 0
    x = input()
    if len(x)!=10 : 
        print('Invalid')
        break 
    for i in x:
        if x.count(i)>1:
            break
        if i.isupper():
            ls['upper'] += 1 
        if i.isdigit():
            ls['digit'] += 1
        if not i.isalnum():
            res = 0
            break
            
            
    if ls['upper']>=2 and ls['digit']>=3 : 
        res = 1
    else : 
        res = 0
    # print(ls)
    if(res==1) : 
        print('Valid') 
    else:
        print('Invalid')
            
