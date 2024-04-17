# https://leetcode.com/problems/string-compression/description/

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        x = chars[0]
        c = 1
        for i in chars[1:] :
            if i==x :
                c += 1
            else : 
                if c==1:
                    s += f'{x}'
                else:
                    s += f'{x}{str(c)}'
                x = i
                c = 1
        
            # print(i,c,x,s)
        if c==1:
            s += f'{x}'
        else:
            s += f'{x}{str(c)}'
        for i in range(len(s)):
            # print(i , s[i])
            # print(i,chars[i])
            chars[i] = s[i]
        # print(s,len(s),)
        return len(s)
        
