# https://leetcode.com/problems/strictly-palindromic-number/

import numpy as np 

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            # print(i)
            base_n=np.base_repr(n,base=i)
            if i==n-2 and base_n == base_n[::-1] :
                return True
            if  base_n != base_n[::-1] :
                return False 
            
