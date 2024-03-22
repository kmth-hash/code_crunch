# https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=study-plan-v2&envId=binary-search

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters : 
            if i>target : 
                return i
        return letters[0]
