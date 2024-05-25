# https://leetcode.com/problems/special-array-i/description/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
         
        for i in range(1,len(nums)) : 
            x = nums[i-1]%2 
            y = nums[i]%2
            # print(nums[i-1] , x , nums[i] , y)
            if (x==0 and y==1) or (x==1 and y==0) : 
                pass
            else : 
                return False
        return True
