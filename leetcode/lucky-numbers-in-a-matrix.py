# https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/?envType=daily-question&envId=2024-07-19

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # print(matrix)
        ls = []
        for row in range(len(matrix)) : 
            ind = matrix[row].index(min(matrix[row]))
            # print(f'lowest at index {ind} for {matrix[row]}')
            mn = matrix[row][ind]
            
            for col in range(len(matrix)) : 
                # print(mn , 'min' ,col,ind,matrix[col][ind])
                temp = matrix[col][ind]
                if temp > mn : 
                    mn = -1 
            if mn not in ls and mn != -1: 
                ls.append(mn)
        return ls
