# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ls = [nums.count(0) , nums.count(1) , nums.count(2)]
        
        for i in range(0,ls[0]):
            nums[i]=0
        for i in range(ls[0],ls[0]+ls[1]):
            nums[i]=1
        for i in range(ls[0]+ls[1],ls[0]+ls[1]+ls[2]):
            nums[i]=2
                    
