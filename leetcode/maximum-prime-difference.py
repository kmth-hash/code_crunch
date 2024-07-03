# https://leetcode.com/contest/weekly-contest-393/problems/maximum-prime-difference/

class Solution:
    
    def isPrime(self ,num):
        if num == 1:
            return False
        elif num > 1:
        
            for i in range(2,num):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        ps = []
        notps = []
        inds = []
        for i in range(len(nums)) : 
            if nums[i] in ps :
                inds.append(i)
            elif nums[i] in notps : 
                pass 
            elif self.isPrime(nums[i]) : 
                ps.append(nums[i])
                inds.append(i)
            else :
                notps.append(nums[i])
            # print(inds , ps , notps)
        if len(inds)>1 :
            return inds[-1]-inds[0]
        return 0
