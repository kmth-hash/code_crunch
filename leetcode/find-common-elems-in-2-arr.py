# https://leetcode.com/problems/find-common-elements-between-two-arrays/

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = [0]*2
        s1 = set(nums1)
        s2 = set(nums2)

        for i in nums1 : 
            if i in s2 : 
                ls[0]+=1

        for j in nums2 :
            if j in s1 : 
                ls[1] += 1
        return ls