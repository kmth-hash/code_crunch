# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)) :
            for j in range(i,len(nums)) : 
                if i!=j and abs(nums[i]-nums[j])==k : 
                    res += 1
        return res
