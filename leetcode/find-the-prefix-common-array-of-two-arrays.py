# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        comp = set()
        for i , num in enumerate(A) : 
            comp.add(num)
            comp.add(B[i])
            res.append(((i+1)*2)-len(comp))
        # print(res)
        return res
