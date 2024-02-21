# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        ls = [n]
        if n==1:
            return True
        while (n!=-1 or n!=1) :
            x = [int(i) for i in str(n)]
            n = sum([i*i for i in x])
            if n in ls : 
                return False
            if n==1:
                return True
            ls.append(n)
            print(ls,x,n)