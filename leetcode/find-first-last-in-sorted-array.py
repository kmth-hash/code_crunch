# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = nums.count(target)
        if c==0:
            return [-1,-1]
        i = nums.index(target)
        return([i,i+c-1])
