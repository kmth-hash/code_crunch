# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        prod = [1 for i in range(ln)]

        temp = 1
        for i in range(ln) : 
            prod[i] = temp 
            temp  *= nums[i] 
            # print(i,temp, prod)
        temp = 1
        for i in range(ln-1,-1,-1) : 
            prod[i] = temp *prod[i]
            temp *= nums[i]
            # print(i,temp ,prod)
        return prod
