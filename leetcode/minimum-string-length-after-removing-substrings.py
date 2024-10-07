# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/

class Solution:
    def minLength(self, s: str) -> int:
        st = []
        while s : 
            if (st and s) :
                
                if (st[-1]=='A' and s[0]=='B') or (st[-1]=='C' and s[0]=='D') : 
                    
                    s = s[1:]
                    st.pop(-1)
                    continue 
            st.append(s[0])
            s = s[1:]
            # print(st,s)
        return len(st)
