# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = []
        v = ['a','e','i','o','u','A','E','I','O','U']
        for i in s:
            if i in v:
                ls.append(i)
        r = ''
        for i in s :
            if i in v:
                r += ls.pop()
            else:
                r += i 
        return r