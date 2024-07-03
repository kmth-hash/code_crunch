# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        for i in nums : 
            if i*-1 in nums : 
                res = max(i , res)
        return res
