# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0)
        for i in range(z):
            nums.remove(0)
        
        nums.extend([0]*z)
        
        