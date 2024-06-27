# https://leetcode.com/problems/find-center-of-star-graph/description/?envType=daily-question&envId=2024-06-27

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        res = set(edges[0])

        for i in edges : 
            res = res.intersection(set(i))
        return res.pop()

  
