# https://leetcode.com/problems/rotate-image/description/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x  = y = len(matrix)-1
        res = []
        for i in range(x+1) : 
            temp = []
            for j in range(y,-1,-1) :
                temp.append(matrix[j][i])
            res.append(temp)
        for i in range(len(res)) : 
            for j in range(len(res[0])) :
                matrix[i][j] = res[i][j]
        
