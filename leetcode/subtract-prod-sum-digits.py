# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ls = [int(i) for i in str(n)]
        return math.prod(ls)-sum(ls)
        
