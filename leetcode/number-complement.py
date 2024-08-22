# https://leetcode.com/problems/number-complement/description/?envType=daily-question&envId=2024-08-22

class Solution:
    def findComplement(self, num: int) -> int:

        return (int(''.join(['1' if i=='0' else '0' for i in bin(num).replace('0b','')]) , 2))

         
