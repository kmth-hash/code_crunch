# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = Counter(s)
        tc = Counter(t)
        res = 0
        # neg = 0
        
        for i in sc : 
            if sc[i]>tc[i] :
                res += sc[i] - tc[i]
            
        return res
