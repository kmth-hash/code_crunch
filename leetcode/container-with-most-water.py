# https://leetcode.com/problems/container-with-most-water/description/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        res = 0
        while left < right : 
            # print(left , right )
            res = max(min(height[left] , height[right] )*(right-left) , res )
            # print(left , right, res)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return res

        