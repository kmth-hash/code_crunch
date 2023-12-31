# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/?envType=daily-question&envId=2023-12-31

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d = dict()
        res = -1
        c = 0 
        for i in s:
            if i in d.keys():
                # d[i] = c
                print('found',i) 
                print('gap',c-1-d[i])
                if res < c-1-d[i]:
                    res = c-1-d[i]
            else:
                d[i]=c
            c+=1
        return res


