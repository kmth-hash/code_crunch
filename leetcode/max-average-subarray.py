# Incomplete 
# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = sum(nums[:k])/k

        for i in range(len(nums)-k+1):
            # print(i,i+k,nums[i:i+k],sum(nums[i:i+k]),k,mx)
            # print(mx, (sum(nums[i:i+k])/k))
            l = (sum(nums[i:i+k])/k)
            mx = max(l,mx)
        # print(mx)
        return mx
