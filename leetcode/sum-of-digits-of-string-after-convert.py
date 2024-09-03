# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        def convert(s) : 
            res = ''
            for letter in s : 
                res += str(ord(letter)-ord('a') + 1)
            # print(res)
            return res
        def transform(s , k ):
            if k==0 : 
                return s 
            return transform(str(sum([int(i) for i in s])),k-1)
        # convert(s)
        return int(transform( convert(s),k))
