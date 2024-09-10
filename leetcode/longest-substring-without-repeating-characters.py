# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ''
        right = 0
        left = 0 
        res = 0
        temp = 0
        for right in s : 
            if right not in subs : 
                subs += right 
                temp += 1
                # print('if',left,right,subs,temp,res)
            else : 
                for i in range(len(subs)) : 
                    if subs[i]==right : 
                        subs = subs[i+1:]+right
                        break 
                temp -= i 
                # print(i,left,right,subs,temp,res)
            res = max(res , temp)
        return res
