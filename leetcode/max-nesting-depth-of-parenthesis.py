# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        ls = []
        for i in s : 
            if i=='(' or i==')' : 
                ls.append(i)
        # print(ls)
        ctr = 0
        mx = 0
        for i in range(len(ls)) : 
            if ls[i]=='(' : 
                ctr += 1
            mx = max(mx , ctr)
            # print(i,ctr,mx)
            if ls[i]==')' : 
                ctr -= 1 


        return mx
