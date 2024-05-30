# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0
        for i in set(nums) : 
            if nums.count(i)==2 : 
                res = res ^ i 
        return res
