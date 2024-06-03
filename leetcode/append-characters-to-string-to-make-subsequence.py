# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        res = len(t)
        for j in s : 
            if j==t[i]:
                # print('found : ',j)
                i += 1
                res -=1
            if i==len(t):
                break
        
        return res
