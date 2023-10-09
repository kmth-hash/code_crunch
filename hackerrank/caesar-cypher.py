#https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true

def caesarCipher(s, k):
    # Write your code here
    def lower(x):
        return x>=97 and x<=122
    def upper(x):
        return x>=65 and x<=90
        
    def cypher(x):
        c = x+k
        if upper(x):
            while not upper(c):
                c-=90-65+1
        if lower(x):
            while not lower(c):
                c-=122-97+1
        return c

    return "".join([chr(cypher(x)) if upper(x) or lower(x) else chr(x) for x in [ord(x) for x in s]])