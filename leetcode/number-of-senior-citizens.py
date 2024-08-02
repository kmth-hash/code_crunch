# https://leetcode.com/problems/number-of-senior-citizens/description/?envType=daily-question&envId=2024-08-01

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def getAge(s) : 
            return int(s[11:13])
        num = 0 
        for i in details : 
            if getAge(i)>60 : 
                num += 1
        return num
