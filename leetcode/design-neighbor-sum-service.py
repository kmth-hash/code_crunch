# https://leetcode.com/problems/design-neighbor-sum-service/description/

class neighborSum:
    grid = []
    length = 0
    def __init__(self, grid: List[List[int]]):
        self.grid = grid 
        self.length = len(grid)
        # print(self.grid)
    def adjacentSum(self, value: int) -> int:
        res = 0
        xCord = yCord = -1 
        for x in range(self.length) : 
            for y in range(self.length) : 
                if value==self.grid[x][y] :
                    xCord = x 
                    yCord = y 
        for x, y in [(xCord-1, yCord), (xCord+1, yCord), (xCord, yCord-1), (xCord, yCord+1)]:
            if 0<= x < self.length and 0 <= y < self.length : 
                res += self.grid[x][y]
        # print(res)
        return res


    def diagonalSum(self, value: int) -> int:
        res = 0
        xCord = yCord = -1 
        for x in range(self.length) : 
            for y in range(self.length) : 
                if value==self.grid[x][y] :
                    xCord = x 
                    yCord = y 
        # print(xCord , yCord)
        for x, y in [(xCord-1, yCord-1), (xCord+1, yCord+1), (xCord+1, yCord-1), (xCord-1, yCord+1)]:
            if 0<= x < self.length and 0 <= y < self.length : 
                res += self.grid[x][y]
        # print(res)
        return res


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
