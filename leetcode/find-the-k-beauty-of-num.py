# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        start = 0
        
        for i in range(len(str(num))):

            if i-start+1 == k :
                s = int(str(num)[start : i+1])
                if( s!=0 and num % s ==0)  : 
                    count += 1     
                # print(start , i , )
                start += 1
        return count
