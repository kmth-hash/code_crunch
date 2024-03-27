# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        start = 0
        tempsum = 0
        for i in range(len(arr)):
            if i-start+1 < k :
                tempsum += arr[i]
                # print('bef',start , i , tempsum)
            if i-start+1 == k :                 
                tempsum += arr[i]
                if tempsum/k >= threshold : 
                    count += 1
                
                tempsum -= arr[start]
                start +=1 
                # print(start , i+1 , tempsum ,arr[start : i+1])
                

        return count 
