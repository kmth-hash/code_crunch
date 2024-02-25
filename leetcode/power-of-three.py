# https://leetcode.com/problems/power-of-three/description/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        n2 = 0
        while n>= x :
            if x==n:
                return True
            n2+=1
            x = pow(3,n2)
            
        return False