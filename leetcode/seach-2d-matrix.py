# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target> matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            if target in matrix[i]:
                return True
        return False