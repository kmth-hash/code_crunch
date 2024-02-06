# https://leetcode.com/problems/count-sorted-vowel-strings/description/

from itertools import combinations_with_replacement
class Solution:
    def valid(self , s :str)->bool :
        for i in range(1,len(s)):
            if s[i-1]>s[i] :
                return False
        return True
    def countVowelStrings(self, n: int) -> int:
        v = ['a','e','i','o','u']
        c = 0
        for i in combinations_with_replacement(v,n):
            if self.valid(''.join(i)) :
                # print(''.join(i))
                c += 1
        return c
