# https://leetcode.com/problems/reverse-prefix-of-word/description

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word : 
            return word
        ind = word.index(ch)+1
        rs = word[: ind][::-1]
        return(rs+word[ind:])
