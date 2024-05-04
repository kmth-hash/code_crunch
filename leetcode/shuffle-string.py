# https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0]*len(s)
        c = 0
        for i in indices : 
            res[i] = s[c]
            c+=  1
        return ''.join(res)
