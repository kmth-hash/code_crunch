# https://leetcode.com/problems/find-the-number-of-winning-players/description/

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        c = 0
        ls = dict()
        for x,y in pick : 
            temp = ls.get(x , -1) 
            if temp==-1 : 
                ls[x] = {y : 1}
            else : 
                temp2 = temp.get(y , -1) 
                if temp2==-1 : 
                    ls[x][y] = 1 
                else : 
                    ls[x][y] += 1 
            # print(ls)
        for k,v in ls.items() : 
            mx = max(v.values()) 
            if k+1<=mx : 
                c+=1

        # print(c)
        return c
