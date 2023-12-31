# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2023-12-31

class Solution:
    def minOperations(self, s: str) -> int:
        x = ''.join(['1' if i%2==0 else '0' for i in range(len(s))])
        y = ''.join(['0' if i%2==0 else '1' for i in range(len(s))])

        
        # print(x,y)
        r1 = 0
        r2 = 0
        for i in range(len(x)):
            # print(x[i] , y[i] , s[i],y[i]!=s[i],r1,r2)
            if x[i]!=s[i]:
                r1+=1
            if y[i]!=s[i]:
                r2+=1
        # print(min(r1,r2))# min(r1,r2))
        return min(r1,r2)

