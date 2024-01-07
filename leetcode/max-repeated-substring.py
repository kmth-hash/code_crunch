#incomplete
#https://leetcode.com/problems/maximum-repeating-substring/description/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ls = sequence.split(word)
        return len(ls)-1

