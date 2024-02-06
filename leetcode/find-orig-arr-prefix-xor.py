# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ls = [pref[0]]
        for i in range(1,len(pref)):
            # x = pref[i-1]^pref[i]
            
            ls.append(pref[i-1]^pref[i])
            
        return(ls)
            
            