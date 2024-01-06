#https://leetcode.com/problems/plus-one/description/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0 :
            return [1]
        s = int(''.join([str(i) for i in digits]))+1
        return [i for i in str(s)]
        
        