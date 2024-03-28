# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left = 0
        subLen = 0
        N = len(nums)
        nums.sort()
        for right in range(N) :
            if nums[right]-nums[left]==1 : 
                subLen = max(subLen , right-left+1)
            while nums[right]-nums[left]>1:
                left += 1
            right += 1
        # print(subLen)
        return subLen
        