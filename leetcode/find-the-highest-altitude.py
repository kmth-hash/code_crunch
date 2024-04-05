# https://leetcode.com/problems/find-the-highest-altitude/description

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        mx = 0
        for i in gain : 
            start += i 
            mx = max(mx , start)
            # print(i,start,mx)
        return(mx)
