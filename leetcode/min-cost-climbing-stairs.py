# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ls = {}

        def dp(num) : 
            if num<2 : 
                return cost[num] 
            if num not in ls : 
                ls[num] = cost[num] + min(dp(num-1) , dp(num-2))
            return ls[num]
        
        ln = len(cost)
        return min(dp(ln-1) , dp(ln-2))
