# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        ls = [i for i in range(n)]
        for i in range(n-2,0,-1):
            ls.append(i)
        w = k % (n+n-2)
        return ls[w]


