#https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true

def gridChallenge(grid):
    # Write your code here
    row = len(grid)
    col = len(grid[0])
    
    new_arr = []
    for item in grid:
        new_arr.append(sorted(item))
        
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(new_arr[j][i])
            
        if temp != sorted(temp):
            return "NO"
        
    return "YES"