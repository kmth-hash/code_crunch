# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        a , b , c = 0 , 1, 1
        if n<3 : 
            return [0,1,1][n]
        while n-2!=0 :
            temp = a+b+c
            a , b, c = b ,c , temp 
            n -= 1 
            print(a,b,c,n,n-3)
        return(c)
