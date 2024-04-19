# https://leetcode.com/problems/max-consecutive-ones-iii/description/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left  = temp = count = 0
        for right in range(len(nums)) : 
            if nums[right]==0 : 
                count += 1
            while count > k : 
                # print('left-->',left,right,nums[left:right+1],count,temp)
                if nums[left]==0 : 
                    count -=1
                left += 1
            
            temp = max(temp , right-left+1)
            # print(left , right ,nums[left : right+1] ,count , temp )
        return temp
