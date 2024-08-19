# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        res = []
        ln1 = len(nums1)
        ln2 = len(nums2)
        while p1<ln1 and p2<ln2 : 
            if nums1[p1]<nums2[p2] : 
                res.append(nums1[p1])
                p1 +=1
            else : 
                res.append(nums2[p2])
                p2 += 1
            # print(p1,p2)
        if p1==ln1 : 
            for i in range(p2 , ln2) : 
                res.append(nums2[i])
        elif p2==ln2 : 
            for i in range(p1 , ln1) : 
                res.append(nums1[i])
        # print(res)
        if (ln1+ln2)%2==0 : 
            mid = (ln1+ln2) //2
            # print(res[mid],res[mid-1] , mid)
            return (res[mid]+res[mid-1])/2
        else : 
            # print(res[(ln1+ln2)//2] , (ln1+ln2)//2)
            return res[(ln1+ln2)//2]
        
