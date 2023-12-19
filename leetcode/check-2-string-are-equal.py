#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ''.join([i for i in word1])
        y = ''.join([i for i in word2])

        if x==y:
            return True
        else:
            return False

