# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        n5 = 0
        n2 = 0
        if n<2 : 
            return 0
        for i in range(2,n+1):
            # print(i , n2,n5)
            while i%2==0 : 
                n2 += 1 
                i = i//2
            while i%5==0 : 
                n5 += 1 
                i = i//5
        
        return min(n2,n5)
            
