# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = [] 

        def recursion(start , rs=[]) : 
            ls.append(rs) 
            for i in range(start , len(nums)) : 
                recursion(i+1 , rs+[nums[i]])
        recursion(0,[])
        return ls 