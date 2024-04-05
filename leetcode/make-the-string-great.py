# https://leetcode.com/problems/make-the-string-great/description/

class Solution:
    def makeGood(self, s: str) -> str:
        ls = [s[0]]

        for i in s[1:] : 
            if ls and ls[-1] == i.swapcase() :
                ls.pop()
            else : 
                ls.append(i)
            # print(ls)
        return ''.join(ls)
