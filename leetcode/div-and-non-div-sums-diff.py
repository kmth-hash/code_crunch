# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        # for i in range(1,n+1):
        #     if i%m==0:
        #         print(res,i,'div')
        #         res -= i 
        #     else :
        #         print(res,i,'notdiv')
        #         res += i 
        res = [-i if i%m==0 else i for i in range(1,n+1)]
        # print(sum(res))

        return sum(res) 

