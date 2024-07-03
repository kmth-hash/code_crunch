# https://leetcode.com/problems/relative-sort-array/?envType=daily-question&envId=2024-06-11

from collections import Counter 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ls = []
        # rs = []
        c1 = Counter(arr1)
        # print(c1)

        for i in arr2 : 
            # print('not found ',i,c1[i])
            for j in range(c1[i]) : 
                ls.append(i)
            del c1[i]
            
        rs = []
        for i in c1 : 
            for j in range(c1[i]) :
                rs.append(i)
        rs.sort()
        # print(rs)
        ls.extend(rs)
        # print(ls,c1)
        return ls
