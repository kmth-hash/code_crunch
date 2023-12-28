#https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        n = nums[0]
        for i in nums[1:]:
            n = max(n+i, i)
            m = max(m,n)
        return m