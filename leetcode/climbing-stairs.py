# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(num):
            nonlocal memo
            if num in [0,1] : 
                return 1 
            if num in memo :
                return memo[num]
            else : 
                memo[num] = dp(num-1)+dp(num-2) 
                return memo[num]
        return dp(n)
