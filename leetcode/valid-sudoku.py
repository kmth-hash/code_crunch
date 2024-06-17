# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(board,rowItr) :
            rows = dict()
            for i in range(9):
                val = rows.get(board[rowItr][i], 0 )+1 
                if val!=1 and board[rowItr][i]!='.' : 
                    # print('Found false ')
                    return False
                rows[board[rowItr][i]] = val
            # print(rows)
            return True

        def checkCol(board,colItr):
            cols = dict()
            for i in range(9) : 
                val = cols.get(board[i][colItr] , 0)+1
                if val!=1 and board[i][colItr]!='.' : 
                    # print('Found False')
                    return False 
                cols[board[i][colItr]] = val
            # print(cols)
            return True 
        
        def checkBlock(board, x, y) : 
            blocks = dict()
            for i in range(x,x+3):
                for j in range(y,y+3):
                    val = blocks.get(board[i][j],0)+1
                    if val!=1 and board[i][j]!='.' :
                        return(False)
                    blocks[board[i][j]] = val 
            # print(blocks)
            return(True)

        for i in range(9) : 
            # val = checkRow(board,i)
            # val = checkCol(board,i)
            if checkRow(board , i) and checkCol(board , i) : 
                pass 
            else : 
                return False
             
            
        for i in range(0,9,3):
            for j in range(0,9,3) : 
                val = checkBlock(board,i,j)  
                if not val : 
                    return False 
               
        return True
