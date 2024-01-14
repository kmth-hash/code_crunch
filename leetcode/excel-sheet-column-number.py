# https://leetcode.com/problems/excel-sheet-column-number/description/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        x = 0
        t = len(columnTitle)-1
        
        for i in range(len(columnTitle)):
            p = pow(26,t)
            v=( p *(ord(columnTitle[i])-64)  )
            x += v
            t-=1
            # print(x,t)
        return x

