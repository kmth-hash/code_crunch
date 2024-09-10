# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        res = 0 

        for i in prices : 
            minPrice = min(minPrice , i)
            res = max(res , i-minPrice)
            # print(minPrice , res , i )
        return res
