# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c = 0
        m = 0 
        for i in s : 
            if i=='R' : 
                c += 1
            elif i=='L':
                c -= 1
            if c == 0 : 
                m += 1
        # print(m)
        return m
