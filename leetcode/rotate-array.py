# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        for i in range(k):
            x = nums.pop()
            # print(nums)
            nums.insert(0,x)
        # print(nums)
