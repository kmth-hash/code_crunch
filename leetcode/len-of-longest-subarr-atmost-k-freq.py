# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = 0
        freq = {}
        for right in range(len(nums)):
            freq[nums[right]]  = freq.get(nums[right] , 0 ) + 1
            if freq[nums[right]] > k : 
                while nums[left] != nums[right] : 
                    freq[nums[left]] -=1 
                    left += 1
                freq[nums[left]] -=1 
                left +=1
            # print(left ,right , nums[left : right+1])
            count = max(count , right-left+1 )
        return count
 
