# https://leetcode.com/problems/xor-queries-of-a-subarray/description

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [arr[0]]
        temp = arr[0]
        for i in range(1,len(arr)) : 
            res.append(res[-1]^arr[i])
        # print(res)
        ls = []
        for l,r in queries : 
            if l==r : 
               ls.append(arr[r])
            elif l==0 : 
                ls.append(res[r])
            else : 
                # print(res[r]^res[l-1]) 
                ls.append(res[r]^res[l-1])
        return ls
