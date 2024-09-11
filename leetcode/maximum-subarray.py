# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -10000
        curr = -10000

        for i in nums : 
            curr = max(curr+i , i)
            sum = max(sum,curr)
        return sum
