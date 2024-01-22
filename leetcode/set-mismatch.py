# https://leetcode.com/problems/set-mismatch/description/?envType=daily-question&envId=2024-01-22

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n2 = 0
        n0 = 0
        nums.sort()
        for i in range(1,len(nums)+1):
            
            c = nums.count(i)
            # print(i,c)
            if c==2:
                n2 = i
            if c==0:
                n0 = i              
            print(i,c,n0,n2)  
        return([n2,n0])

