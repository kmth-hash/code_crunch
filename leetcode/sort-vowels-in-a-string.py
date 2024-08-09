https://leetcode.com/problems/sort-vowels-in-a-string/description/

class Solution:
    def sortVowels(self, s: str) -> str:
        v = []
        res = ''
        for i,l in enumerate(s.lower()):
            if l in 'aeiou' :
                v.append(s[i])
        v.sort()
        for i,l in enumerate(s.lower()) : 
            if l in 'aeiou' : 
                res += v.pop(0)
            else : 
                res += s[i]
            # print(res)
        s = res
        del v
        return res
