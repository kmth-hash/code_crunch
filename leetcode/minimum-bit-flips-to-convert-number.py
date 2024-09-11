# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        x1 = bin(start)[2:]
        x2 = bin(goal)[2:]
        ln = max(len(x1) , len(x2))
        x1 = x1.zfill(ln)
        x2 = x2.zfill(ln)
        # print(ln,x1,x2)
        return sum([1 if x1[i]!=x2[i] else 0 for i in range(ln) ])
        
