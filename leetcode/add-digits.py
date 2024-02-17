# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num))!=1:
            num = sum([int(i) for i in str(num)])
            # print(num)
        return(num)