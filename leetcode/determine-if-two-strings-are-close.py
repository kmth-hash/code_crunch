# https://leetcode.com/problems/determine-if-two-strings-are-close/description/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1 = dict()
        d2 = dict()
        l1 = len(word1)
        l2 = len(word2)
        ds1 = set(word1)
        ds2 = set(word2)

        if l1!=l2 : 
            return False 
        for i in word1 : 
            d1[i] = d1.get(i , 0)+1
            if i not in ds2 : 
                return False
        for i in word2  :
            d2[i] = d2.get(i,0)+1
            if i not in ds1 : 
                return False
        
        l1 = sorted(d1.values())
        l2 = sorted(d2.values())
            
        return l1==l2
        

