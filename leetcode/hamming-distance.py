# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ls = bin(x).replace('0b','')
        rs = bin(y).replace('0b','')
        # print(ls,rs)
        if len(ls)>len(rs):
            x = ls 
            y = rs 
            y = '0'*(len(ls)-len(rs))+rs
            # print(str(x) , str(y),'z1')
        else:
            x = rs
            y = ls
            y = ('0'*(len(rs)-len(ls)))+ls 
            # print(str(x) , str(y),'z2',('0'*(len(rs)-len(ls)))+ls)
        t = 0
        x = str(x)
        y = str(y)
        for i in range(len(x)):
            if x[i]!=y[i] : 
                t += 1
            
        return t
