#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    string=string.lower()
    a = 0
    b = 0
    v = ['a','e','i','o','u']
    for i in range(len(string)):
        #print(string[i])
        if(string[i] in v):
            b = b + (len(string)-i)
        else:
            a = a + len(string) - i
    #print(a,b)
    if a>(b):
        print('Stuart',(a))
    elif (b)>(a):
        print('Kevin',(b))
    else:
        print('Draw')

