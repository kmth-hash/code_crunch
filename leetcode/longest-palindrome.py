# https://leetcode.com/problems/longest-palindrome/description/
class Solution:
    def longestPalindrome(self, s: str) -> int:
        t = set([i for i in s])
        drep = dict()
        dnon = dict()
        for i in t : 
            temp_counter = s.count(i)
            if temp_counter%2==0:
                drep[i] = temp_counter
            else:
                drep[i] = temp_counter-1
                dnon[i] = 1
        # print(drep , dnon, t,sep='\n')
        if sum(dnon.values())>0:
            return sum(drep.values())+1
        else:
            return sum(drep.values())