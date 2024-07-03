# https://leetcode.com/problems/harshad-number/description/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res= sum([int(i) for i in str(x)])
        if x%res==0:
            return res
        else:
            return -1
