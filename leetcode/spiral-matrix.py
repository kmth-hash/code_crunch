# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        ls = []
        dir = 0 
        top , bottom , left , right = 0, rows-1 , 0 , cols-1

        while top<=bottom and left<=right : 
            # print(top , bottom , left , right)
            if dir==0 : 
                for i in range(left , right+1) : 
                    ls.append(matrix[top][i])
                top += 1                 
            elif dir==1 : 
                for i in range(top , bottom+1) :
                    ls.append(matrix[i][right])
                right -= 1
            elif dir ==2 : 
                for i in range(right,left-1,-1) : 
                    ls.append(matrix[bottom][i])
                bottom -= 1
            else : 
                for i in range(bottom , top-1,-1) : 
                    ls.append(matrix[i][left])
                left += 1
            dir += 1 
            dir %= 4 
        # print(ls)
        return ls
