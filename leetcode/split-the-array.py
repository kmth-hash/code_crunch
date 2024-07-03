# https://leetcode.com/problems/split-the-array/description/

# class Solution:
#     def isPossibleToSplit(self, nums: List[int]) -> bool:
#         d = dict()
#         for i in nums : 
#             d[i] = d.get(i , 0)+1
#         for v in d.values():
#             if v>2 : 
#                 return False
#         return True

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        d = dict()
        for i in nums : 
            d[i] = d.get(i , 0)+1
            if d[i]>2 : 
                return False
        return True
