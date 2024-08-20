# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        ls=["","","abc","def","ghi","jkl", "mno", "pqrs", "tuv", "wxyz"]

        def dp(i,itr, rs):
            nonlocal res
            rs += itr 
            # print(rs)
            
            if i==len(digits) : 
                # print('res break --> ',rs)
                res.append(rs)
                return 
            
            for elem in ls[int(digits[i])] : 
                dp(i+1 , elem , rs)
        if digits=='' : 
            return []
        for i in ls[int(digits[0])] : 
            dp(1 , i, '')

        return res
