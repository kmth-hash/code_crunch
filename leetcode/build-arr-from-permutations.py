# https://leetcode.com/problems/build-array-from-permutation/submissions/1134646181/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        print(res)
        return res

