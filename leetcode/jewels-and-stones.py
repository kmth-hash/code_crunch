# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = 0
        for i in stones :
            if i in jewels : 
                n += 1 
        return n
