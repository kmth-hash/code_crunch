# https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n: int) -> str:
        
        start = '1'
        def sayWords(s) : 
            prev = s[0]
            # print(f'-----> {s}')
            curr = ''
            counter = 1
            finalStr = ''
            if len(s)==1 : 
                return f'1{s}'
            for j in s[1:] : 
                curr = j
                if curr!=prev : 
                    finalStr += f'{counter}{prev}'
                    counter = 1
                else : 
                    counter+=1 
                prev = curr
            finalStr += f'{counter}{prev}'
            # print(s,finalStr)
            return finalStr
        if n==1 : 
            return "1"
        for i in range(n-1) : 
            # print(start)
            try :
                start = sayWords(start)
            except Exception as ex : 
                # print(ex)
                pass
            
        return start
        
