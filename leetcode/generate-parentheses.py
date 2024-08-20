# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dp(left , right,rs):
            if left==n and right == n :
                # print('res break-->' , rs)
                res.append(rs)
                return 
            # print(left,right,rs)
            if left+1<=n : 
                dp(left+1, right , rs+'(')
            if right+1<=n and right+1<=left: 
                dp(left,right+1, rs+')')
        dp(1,0,'(')
        return res

