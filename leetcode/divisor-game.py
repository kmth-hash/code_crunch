# https://leetcode.com/problems/divisor-game/description/

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n&1 : 
            return False 
        return True
