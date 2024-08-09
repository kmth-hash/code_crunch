# https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checkvalid(m) : 
            s = set()
            if m[1][1]!=5:
                return 0
            for i in m : 
                for j in i : 
                    if 1<=j<=9 : 
                        s.add(j)
                    else : 
                        return 0
            if len(s)!=9 : 
                return 0
            # Check sum of diagonals , rows and columns
            if (m[0][0]+m[1][1]+m[2][2])==(m[2][0]+m[1][1]+m[0][2])==(m[0][1]+m[0][0]+m[0][2])==(m[1][0]+m[1][1]+m[1][2])==(m[2][0]+m[2][1]+m[2][2])==(m[1][0]+m[0][0]+m[2][0])==(m[0][1]+m[1][1]+m[2][1])==(m[0][2]+m[1][2]+m[2][2]) :
                # print('Found' , m)
                return 1
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        # print(grid)
        if rows<3 or cols<3 : 
            return 0
        tempGrid= []
        visited = [[0 for i in range(cols)] for j in range(rows)]
        # print('Grid dimension : ',len(grid) , len(grid[0]))
        # print('visited dimension : ',len(visited) , len(visited[0]))
        # print(visited)
        x = y = res = 0
        for i in range(rows-3+1) : 
            for j in range(cols-3+1) : 
                
                
                visitFlag = sum([sum(x[j:j+3]) for x in visited[i:i+3]])
                
                tempGrid = [x[j:j+3] for x in grid[i:i+3]]
                if checkvalid(tempGrid)==1 : 
                    res += 1 
                    # print(visitFlag,'-->flag',visited,i,j)
                    for a in range(i,i+3) : 
                        for b in range(j,j+3) : 
                            # print(a,b,i,j)
                            visited[a][b] = 1 
                y+=1
        return res
