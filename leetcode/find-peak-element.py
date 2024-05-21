# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peakEle = nums[0]
        peakInd = 0
        for i , ctr in enumerate(nums):
            if ctr>peakEle : 
                peakEle = max(peakEle , ctr)
                peakInd = i
        return peakInd
