# https://leetcode.com/problems/single-number-iii/description/

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ls = Counter(nums)
        res = []
        for x in ls.keys(): 
            if ls[x]==1:
                res.append(x)
        return res
