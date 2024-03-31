# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/description/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 999 
        if len(nums)==0 :
            return -1
    
        for i in range(len(nums)) : 
            tempres = 0
            for j in range(i , len(nums)) : 
                
                tempres  = tempres | nums[j]
                if tempres >= k : 
                    res = min(res , j-i+1)
                    
       
        if res==999 : 
            return -1
        return res 
