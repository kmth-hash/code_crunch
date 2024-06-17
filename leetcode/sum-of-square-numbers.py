# https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17

from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0,int(sqrt(c))+1):
            j = sqrt(c- i*i)
            if j==int(j):
                return True
        return False
