# https://leetcode.com/problems/find-the-encrypted-string/description/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        return s[k%len(s):]+s[:k%len(s)]
