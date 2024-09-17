# https://leetcode.com/problems/uncommon-words-from-two-sentences/description

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter 
        c1 = Counter([i for i in s1.split(' ')])
        c2 = Counter([i for i in s2.split(' ')])
        c1 = c1+c2
        # res = []
        # for k in c1.keys() : 
        #     # print(k,c1[k])
        #     if c1[k]==1 : 
        #         res.append(k)
        # return res
        return [k for k in c1.keys() if c1[k]==1]
