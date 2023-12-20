# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)
        # print(x)
        for i in range(len(nums)):
            for j in range(len(nums)):
                # print(nums[i],nums[j],x)
                if nums[i]>nums[j]:
                    x[i]+=1

        # print(x)
        return x
