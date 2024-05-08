# https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = score
        res = sorted(score , reverse=True)
        d = dict()
        for i , num in enumerate(res):
            print(i+1,num)
            d[num] = i+1
        
        for i in range(len(score)):
            if score[i] == res[0] :
                score[i] = 'Gold Medal'
            elif score[i] == res[1] :
                score[i] = 'Silver Medal'
            elif score[i] == res[2] : 
                score[i] = 'Bronze Medal'
            else:
                score[i] = str(d[score[i]])
        return score
