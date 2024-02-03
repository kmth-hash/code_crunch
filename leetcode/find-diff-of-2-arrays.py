# https://leetcode.com/problems/find-the-difference-of-two-arrays/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ls = set(nums1)-set(nums2)
        rs = set(nums2)-set(nums1)

        return [list(ls) , list(rs)]