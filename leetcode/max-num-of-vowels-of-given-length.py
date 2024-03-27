# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        count = 0
        tempcount = 0

        for i in range(len(s)):
            if i-start+1<k :
                if s[i] in 'aeiou' :
                    tempcount += 1  
                # print('bef',start , i , tempcount , count ,s[i] , s[start:i+1])
            if i-start+1==k:
                if s[i] in 'aeiou':
                    tempcount += 1                
                
                count = max(count , tempcount)
                if s[start] in 'aeiou':
                    tempcount -= 1
                start += 1
                # print('aft',start , i , tempcount , count, s[i] , s[start:i+1] , s[start])
                
        return count
