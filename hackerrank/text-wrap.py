#https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    s = ''
    for i in range(len(string)):
        if i % max_width==0:
            s = s+'\n'
        s = s + string[i]
    s = s[1:]
    return s 

