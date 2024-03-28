# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l1 = []
        l2 = []
        for i in range(len(s1)) :
            if s1[i]!=s2[i]:
                l1.append(s1[i])
                l2.append(s2[i])
        if len(l1)== 0 and len(l2)==0 : 
            return True
        if len(l1)>2 or len(l2)>2 : 
            return False
        for i in l1:
            if i not in l2 :
                return False 
        return True