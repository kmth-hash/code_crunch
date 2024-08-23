# https://leetcode.com/problems/fraction-addition-and-subtraction/description/?envType=daily-question&envId=2024-08-23

class Solution:
    def fractionAddition(self, expression: str) -> str:
        ls = []
        temp = ''
        if expression[0].isdigit(): 
            expression = f'+{expression}'
        for i in range(len(expression)-1, -1 ,-1) :
            if expression[i] =="-" :
                if temp in ls : 
                    ls.remove(temp)
                else : 
                    ls.append(expression[i]+temp)
                temp = ''
            elif expression[i]=='+' : 
                if '-'+temp in ls : 
                    ls.remove('-'+temp)
                else : 
                    ls.append(temp)
                temp = ''
            else : 
                temp = expression[i]+temp
            # print(temp,ls)
        if temp : 
            ls.append(temp)
        # print(ls)

        def solve(ls) : 
            num , den = 0,1 
            for elem in ls : 
                n , d = map(int , elem.split('/'))
                # print(elem , n,d , elem.split('/'))
                num = num*d + den*n 
                den = den * d 
                # print(num , den ,'intermediate')
            x = gcd(num,den)
            return (f'{num//x}/{den//x}')
        return solve(ls)
