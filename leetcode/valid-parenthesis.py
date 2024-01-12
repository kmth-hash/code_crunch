# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        if s[0]=='}' or s[0]==']' or s[0]==')':
            return False
        for i in s:
            if i=='(' or i=='{' or i=='[':
                ls.append(i)
            elif i==')':
                if len(ls)==0:
                    return False
                if i==')' and ls[-1]=='(':
                    ls.pop(-1)
                else:
                    return False
            elif i=='}':
                if len(ls)==0:
                    return False
                if i=='}' and ls[-1]=='{':
                    ls.pop(-1)
                else:
                    return False
            elif i==']':
                if len(ls)==0:
                    return False
                if i==']' and ls[-1]=='[':
                    ls.pop(-1)
                else:
                    return False
        if len(ls)==0:
            return True
                