# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()
        for i in nums :
            d[i] = d.get(i,0)+1
            # print(t,i)
            if d[i]==2:
                # print('found',i)
                return i
    
