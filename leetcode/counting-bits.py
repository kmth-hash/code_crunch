# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def count1s(self , s):
        return str(s).count('1')
    def countBits(self, n: int) -> List[int]:
        ls = []
        for i in range(n+1):
            ls.append( self.count1s(str(bin(i).replace('0b',''))) )
        return ls