# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/

class Solution:
    def getSmallestString(self, s: str) -> str:
        diff = s 
        
        for i in range(1,len(s)) :
            if int(s[i])%2==int(s[i-1])%2  : 
                # print(i,i-1)
                # print(s[:i-1],s[i],s[i-1],s[i+1:])
                temp = str(s[:i-1]+s[i]+s[i-1]+s[i+1:])
                # print(temp)
                diff = min(diff , temp)
        return diff
        
