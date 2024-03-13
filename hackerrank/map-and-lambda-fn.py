# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n==0:
        return []
    # if n==1:
    #     return [0]
    # if n==2:
    #     return [0,1]
    
    
    ls = [0,1]
    if n<=2 :
        return ls[:n]
    for i in range(2,n):
        ls.append(ls[i-1]+ls[i-2])
        # print(ls) 
    return ls

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
