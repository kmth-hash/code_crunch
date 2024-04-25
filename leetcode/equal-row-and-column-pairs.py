# https://leetcode.com/problems/equal-row-and-column-pairs/description

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = []
        ln = len(grid)
        res = 0
        for i in range(ln):
            ctemp = []
            for j in range(ln) : 
                ctemp.append(grid[j][i])
            if ctemp in grid :
                d = grid.count(ctemp)
                res += d
        
        # print(cols)
        return res
