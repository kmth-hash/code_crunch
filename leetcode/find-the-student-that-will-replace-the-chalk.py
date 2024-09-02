# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalCost = sum(chalk)

        k = k%totalCost
        # print(k , totalCost)
        res = 0
        for i in range(len(chalk)) : 
            # print(i , k , chalk[i])
            if k-chalk[i]<0 : 
                res = i
                break
            k -= chalk[i]
        return res
