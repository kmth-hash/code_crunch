# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ls = [bank[0].count('1')]
        res = 0
        for i in range(1 , len(bank)) : 
            lasers = bank[i].count('1')
            if lasers ==0 : 
                continue 
            else : 
                res += (ls[-1] * lasers) 
                ls.append(lasers)
        return res
