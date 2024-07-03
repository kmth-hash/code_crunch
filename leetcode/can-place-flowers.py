# https://leetcode.com/problems/can-place-flowers/description/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        ln = len(flowerbed)
        for i in range(ln) : 
            if flowerbed[i] ==0 and (i==0 or flowerbed[i-1]==0) and (i==ln-1 or flowerbed[i+1]==0):
                flowerbed[i]=1
                n -= 1
                if n==0 : 
                    return True
        return False
