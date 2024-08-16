# https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        tempMin , tempMax , res = inf , -inf , 0
        for i in range(len(arrays)) : 
            
            res = max( arrays[i][-1] - tempMin , tempMax - arrays[i][0] ,res)
            tempMin ,tempMax = min(tempMin, arrays[i][0]),max(tempMax , arrays[i][-1])
            

        return res
