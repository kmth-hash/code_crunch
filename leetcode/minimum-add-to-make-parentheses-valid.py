# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = []
        counter = 0
        for i in s : 
            if i =='(' : 
                st.append(i)
            else : 
                if st and  st[-1]=='(' : 
                    st.pop()
                else : 
                    counter += 1 
            # print(i,st,counter)
        return counter+len(st)
