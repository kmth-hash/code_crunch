# https://leetcode.com/contest/weekly-contest-393/problems/latest-time-you-can-obtain-after-replacing-characters/

class Solution:
    def findLatestTime(self, s: str) -> str:
        res = ''
        v = [1,9,':',5,9]
        if s[0]=='0':
            v[1] = 9
        else:
            v[1] = 1
        if s[1]!='?' and int(s[1])>1:
            v[0]=0
        for tt in range(len(s)):
            if tt==2:
                res += ':'
                continue 


            if s[tt]=='?':
                res += str(v[tt])

            else:
                res += s[tt]
        return(res)
