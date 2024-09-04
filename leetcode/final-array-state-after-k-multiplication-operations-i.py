# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k) : 
            mn = nums.index(min(nums))
            nums[mn] = nums[mn]*multiplier
            # print(nums,mn)
        return nums
