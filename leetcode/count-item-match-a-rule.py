#https://leetcode.com/problems/count-items-matching-a-rule/description/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0

        for t,c,n in items:
            if ruleKey =='color' and ruleValue==c:
                res+=1
            elif ruleKey=='type' and ruleValue==t:
                res += 1
            
            elif ruleKey=='name' and ruleValue==n:
                res += 1
            # print(t,c,n,res)
        return res