# https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints))!=len(timePoints):
            return 0
        ls = [ x[0]*60+x[1] for x in [list(map(int, i.split(':'))) for i in timePoints] ]
        ls = sorted(ls)
        mn = 1400 
        # print(ls)
        for i in range(len(ls)):
            if i==0 :
                # print(abs(ls[i]-ls[i-1]), abs(1440-ls[i-1]),mn)
                mn = min(1440-ls[-1]+ls[0],mn)
            else :
                # print(mn,abs(ls[i]-ls[i-1]))
                mn = min(mn,abs(ls[i]-ls[i-1]))
        return mn
