# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        start = 0

        for i in range(len(s)):
            if i-start+1 ==3 :
                # print(s[start : i+1])
                if s[start] != s[start+1] and s[start+2] != s[start+1] and s[start] != s[start+2] : 
                    count += 1
                start += 1
        return count
