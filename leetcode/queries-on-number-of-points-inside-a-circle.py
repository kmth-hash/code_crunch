# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ls=[]
        for i in queries:
            counter=0
            for j in points:
                if ((((i[0]-j[0])**2)+((i[1]-j[1])**2))**0.5)<=i[2]:
                    counter+=1
            ls.append(counter)
        return ls
