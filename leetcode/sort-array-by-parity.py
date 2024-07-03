# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in nums : 
            if i%2==0 : 
                evens.append(i)
            else : 
                odds.append(i)
        evens.extend(odds)
        return evens
