# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        ls = [nums.count(i) for i in set(nums)]
        # print(ls)

        ls.sort()
        return ls.count(ls[-1])*ls[-1]

