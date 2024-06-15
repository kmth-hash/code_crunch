# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        m = 0

        ls = []
        for i in range(len(nums)):
            if nums[i]==x:
                ls.append(i)
                m+=1
        # print(ls , m)
        
        res = []
        for i in queries : 
            if i<=m:
                res.append(ls[i-1])
            else:
                res.append(-1)
        # print(res)
        return res
