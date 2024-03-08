# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.strip().split(' ')
        # print(r)
        return ' '.join([i.strip() for i in r[::-1] if i!=''])
