# https://leetcode.com/problems/valid-word/description/

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3 : 
            return False 
        d = dict()
        vowels = 'aeiouAEIOU'
        for i in word : 
            if i.isalnum():
                if i in vowels and i.isalpha(): 
                    d['v'] = d.get('v',0)+1
                elif i.isalpha() : 
                    d['c'] = d.get('c',0)+1
                else : 
                    d['n'] = d.get('n',0)+1
                
            else : 
                return False
        # print(d)
        if d.get('v',0)>=1 and d.get('c',0)>=1 :
            return True
        return False
