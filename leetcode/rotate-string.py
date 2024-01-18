# https://leetcode.com/problems/rotate-string/description/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = 0 
        ls = s 
        for i in range(len(s)):
            print(s[x:]+s[:x])
            rs = s[x:]+s[:x]
            if rs == goal : 
                return True
            x += 1
        return False