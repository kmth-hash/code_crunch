# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n) ]
        # print(matrix)

        top , bottom , left , right = 0 , n-1 , 0 , n-1
        counter = 1
        while top<=bottom and left<=right : 
            for i in range(left , right+1) : 
                matrix[top][i] = counter
                counter += 1 
            # print(matrix,top , bottom , left , right)
            top += 1 
            for i in range(top,bottom+1) : 
                matrix[i][right] = counter 
                counter += 1 
            # print(matrix,top , bottom , left , right)
            right -=1 
            for i in range(right,left-1,-1) :
                matrix[bottom][i] = counter 
                counter += 1
            # print(matrix,top , bottom , left , right)
            bottom -= 1
            for i in range(bottom,top-1,-1) : 
                matrix[i][left] = counter 
                counter += 1
            # print(matrix,top , bottom , left , right)
            left += 1 
        return matrix
