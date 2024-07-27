# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        
        for m in words : 
            temp = ''
            for letter in m : 
                temp += (morseCodes[ord(letter)-ord('a')])
            res.append(temp)
        
        return len(set(res))
