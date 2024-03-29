# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s1 = s.count('1')
        if s1==1:            
            return s.replace('1','')+'1'
        s0 = s.count('0')
        return (s1-1)*'1'+s0*'0'+'1'