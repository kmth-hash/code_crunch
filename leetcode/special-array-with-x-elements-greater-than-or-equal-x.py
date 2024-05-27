# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/?envType=daily-question&envId=2024-05-27

class Solution:
    def specialArray(self, nums: List[int]) -> int:

        for i in range(1,len(nums)+1):
            res = sum(1 for j in nums if j>=i)
            # print(res)

            if res==i :
                return res
        return -1
