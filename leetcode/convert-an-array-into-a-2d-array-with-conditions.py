# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        while nums : 
            ls = []
            for i in range(len(nums)-1, -1, -1):
                # print(i)
                if nums[i] not in ls :
                    ls.append(nums[i])
                    nums.pop(i)
                # print(ls,nums)
            res.append(ls)
        return res
