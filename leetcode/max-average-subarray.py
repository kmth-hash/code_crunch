# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        curr = res
        for i in range(k,len(nums)) : 
            curr = curr +(nums[i]-nums[i-k])
            res = max(res , curr)
            
        # print(res/k)
        return res/k
