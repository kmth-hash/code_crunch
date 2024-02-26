# https://leetcode.com/problems/power-of-four/description/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        x = 1
        n2 = 0
        while n>= x :
            if x==n:
                return True
            n2+=1
            x = pow(4,n2)
            
        return False
