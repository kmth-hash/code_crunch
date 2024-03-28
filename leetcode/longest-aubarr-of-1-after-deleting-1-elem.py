# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        flag = 0

        for right in range(len(nums)) : 
            
            if nums[right] ==0 :
                flag += 1
                while flag>1: 
                    if nums[left]==0:
                        flag -=1

                    left += 1
                
            count = max(count , right-left)     
            # print(left , right , count , nums[left:right+1])
        return count 
            
        