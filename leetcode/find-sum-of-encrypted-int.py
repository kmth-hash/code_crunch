# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for i in range(len(nums)): 
            n= len(str(nums[i]))
            m = max(str(nums[i]))
            nums[i] = int( n*str(m) )
        # print(nums)
        return sum(nums)
