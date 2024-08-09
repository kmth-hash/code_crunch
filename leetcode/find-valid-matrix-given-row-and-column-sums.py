# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/?envType=daily-question&envId=2024-08-09

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rr , cc = len(rowSum) , len(colSum) 
        ls = [[0 for i in range(cc)] for j in range(rr)]
        # print(ls) 

        rr -= 1
        cc -= 1
        while rr>=0 and cc>=0 : 
            if rowSum[rr]<=colSum[cc] : 
                ls[rr][cc] = rowSum[rr] 
                colSum[cc] -= rowSum[rr]
                rr -= 1 
            else : 
                ls[rr][cc] = colSum[cc]
                rowSum[rr] -= colSum[cc]
                cc -= 1
            # print(ls)
        return ls 
