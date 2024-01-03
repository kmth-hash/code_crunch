# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        # print(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]==nums[j] and i<j):
                    res+=1
        return res 
