# https://leetcode.com/problems/find-the-key-of-the-numbers/description/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 , num2 , num3 = str(num1).zfill(4),str(num2).zfill(4),str(num3).zfill(4)
        # print(num1,num2,num3)
        # res = []
        # for i in range(4) : 
        #     res.append(min(num1[i],num2[i],num3[i]))
        # return int(''.join(res))

        return int(''.join([min(num1[i],num2[i],num3[i]) for i in range(4) ]))
