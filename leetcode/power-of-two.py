https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        n2 = 0
        while n>= x :
            if x==n:
                return True
            n2+=1
            x = pow(2,n2)
            
        return False