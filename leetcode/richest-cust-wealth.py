# https://leetcode.com/problems/richest-customer-wealth/description/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = sum(accounts[0])
        for acc in accounts :
            m = max(m , sum(acc))
    
        return m