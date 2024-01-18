# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        rs = []
        for i in words : 
            for j in words :
                if i!=j :
                    if i in j :
                        rs.append(i)
                        break
        return(rs)