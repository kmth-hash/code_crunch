# https://leetcode.com/problems/three-consecutive-odds/submissions/1305891174/?envType=daily-question&envId=2024-07-01

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = len(arr)
        if l<3 : 
            return False 
        if l==3 : 
            if 0 in [arr[0]%2 , arr[1]%2 , arr[2]%2] : 
                return False 
            else : 
                return True  
        for i in range(3 , l+1) : 
            if 0 in [arr[i-3]%2 , arr[i-2]%2 , arr[i-1]%2] : 
                # print(arr[i-3:i] , True )
                pass 
            else : 
                # print(arr[i-3:i] , False)
                return True 
        return False
