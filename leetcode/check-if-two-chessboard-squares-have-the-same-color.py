# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        
        def getColor(cell) : 
            col = ord(cell[0])-ord('a')
            row = int(cell[1])-1
            if row%2==1 : 
                if col%2==1 : 
                    return 0 
                else : 
                    return 1 
            else : 
                if col%2==1 : 
                    return 1
                else : 
                    return 0 

        return getColor(coordinate1)==getColor(coordinate2)
