# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c = 0 
        res = ""
        ind = ""
        for i in s : 
            # print("i",i)
            # print(ind , res , i , s,c)
            if c==0:
                
                res += ind[1:-1]
                ind = ""
            if i=='(':
                c +=1
                ind += i
            else :
                c -=1
                ind += i
        
        res += ind[1:-1]
        print(ind , ":",res , i ,s ,c)
        return res