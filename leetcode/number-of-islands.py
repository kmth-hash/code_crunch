# https://leetcode.com/problems/number-of-islands/description

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def printGrid() : 
            for row in grid : 
                for cell in row : 
                    print(cell , end='-')
                print('')
            print('\n')
        
        

        res = 0 
        maxX = len(grid[0])
        maxY = len(grid)
        if not grid :
            return 0 
        def dfs(i ,j) : 
            nonlocal maxX , maxY
            # printGrid()
            if i<0 or j<0 or i>=maxY or j>=maxX or grid[i][j]=='0' : 
                # print(i,j)
                return 
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)



        for i in range(maxY): 
            for j in range(maxX) : 
                if grid[i][j] == '1' : 
                    dfs(i,j) 
                    res += 1
        return res
