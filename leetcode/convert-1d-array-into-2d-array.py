# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=daily-question&envId=2024-09-01

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ln = len(original)
        if ln!=m*n : 
            return []
        # res = []
        # for line in range(0,ln , n) : 
        #     res.append(original[line : line+n])
        # return res

        return [original[line : line+n] for line in range(0,ln,n)]
