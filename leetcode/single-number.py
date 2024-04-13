# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set(nums)
        for i in d : 
            if nums.count(i)==1:
                return i
        return -1
