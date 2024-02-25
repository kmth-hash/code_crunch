# https://leetcode.com/problems/zigzag-conversion/description/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        res = [[] for _ in range(numRows)]
        # print(res , 'res')
        c = 0
        # for i in range(1,len(s)):
        #     n = (2*numRows - 2)
        #     print(i , n ,i%n )
        #     x=i%n
        #     print(x%(n/2))
        res[0].append(str(s[c]))
        # print(0 ,str( s[c]),c )

        c+=1
        for j in range(len(s)):
            for i in range(1, numRows):
                if c==len(s):
                    break
                # print(i ,str( s[c]),c )
                res[i].append(str(s[c]))
                c+=1
            for i in range(numRows-2 , -1 , -1):
                if c==len(s):
                    break
                # print(i, str(s[c]),c)
                res[i].append(str(s[c]))
                c+=1
            
        # print(res)
        resStr = ''
        for i in res : 
            resStr += ''.join(i)
        return resStr