# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        t2 = s
        if s=='' :
            return True

        for i in t : 
            if t2=='':
                break
            if i==t2[0] : 
                t2 = t2[1:]
            # print(i,t2)
        if len(t2)==0:
            return True
        return False
        
        
