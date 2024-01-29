# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        l1 = len(word1)
        l2 = len(word2)
        for i in range(max(len(word2) , len(word1))):
            if i<l1:
                res += word1[i]
            if i<l2:
                res += word2[i]
        return(res)