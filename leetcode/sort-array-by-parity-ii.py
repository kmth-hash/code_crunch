# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        stack = [-1] * len(nums)
        # print(stack)
        evenItr = 0
        oddItr = 1
        for i in range(len(nums)) : 
            if nums[i]%2==0 : 
                stack[evenItr] = nums[i]
                evenItr += 2
            else : 
                stack[oddItr] = nums[i] 
                oddItr += 2 
        return(stack)
