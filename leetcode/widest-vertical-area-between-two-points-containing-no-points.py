# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ls = []
        for x,y in points :
            ls.append(x)
        ls.sort()
        mx = 0
        for i in range(0,len(ls)-1):
            mx = max(mx , ls[i+1]-ls[i])
            # print(mx)
        return mx

