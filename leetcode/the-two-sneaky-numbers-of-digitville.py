# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums : 
            if n not in d : 
                d[n] = 1
            else : 
               res.append(n)
        return res 
