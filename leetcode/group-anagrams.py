# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for i in strs : 
            k = ''.join(sorted(i))
            temp = d.get(k , [])
            temp.append(i)
            d[k] = temp
            
                
        return d.values()

        
