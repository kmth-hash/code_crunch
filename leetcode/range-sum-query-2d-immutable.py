# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m=[[0] * (len(matrix[0])+1) for i in range(len(matrix)+1)]
        
        for r in range(len(self.m)-1):
            for c in range(len(self.m[0])-1):
                self.m[r+1][c+1]=matrix[r][c] + self.m[r][c+1] + self.m[r+1][c] - self.m[r][c]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x =  self.m[row2+1][col2+1] - self.m[row1][col2+1] - self.m[row2+1][col1] + self.m[row1][col1]
        return x
