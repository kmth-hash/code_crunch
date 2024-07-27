# https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisks = 0
        flag = 0
        for i in s : 
            if flag==0: 
                if i=='*' : 
                    asterisks += 1
                    
                elif i=='|' : 
                    flag = 1 
                
            else : 
                if i=='|' : 
                    flag = 0 

        return asterisks
