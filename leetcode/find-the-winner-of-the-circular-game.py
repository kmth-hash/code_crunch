# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        curr = 0
        while len(arr)!=1 : 
            curr = (curr + k -1 ) %len(arr)
            # print(arr[curr-1] , arr , curr )
            arr.pop(curr)
        return arr[0]    
