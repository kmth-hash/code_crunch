# https://leetcode.com/problems/height-checker/?envType=daily-question&envId=2024-06-10

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ls = heights.copy()
        ls.sort()
        
        res = sum([1 for i in range(len(ls)) if ls[i]!=heights[i] ])
        return res
