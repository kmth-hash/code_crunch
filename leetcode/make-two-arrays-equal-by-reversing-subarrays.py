# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr : 
            if i in target : 
                target.remove(i)
        return len(target)==0 

      # return Counter(arr)==Counter(target)
