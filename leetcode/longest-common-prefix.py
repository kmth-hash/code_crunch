#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if len(strs)==0 or "" in strs:
            return res
        strs.sort()
        for i in range(len(strs[0])):
            print(strs[0][i] , strs[-1][i])
            if strs[0][i]==strs[-1][i]:                
                res+=strs[0][i]
                print('res',res)
            else:
                break
        return res
        print('end',res)
            
        