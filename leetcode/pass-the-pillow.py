# https://leetcode.com/problems/pass-the-pillow/description

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        ls = [i for i in range(1,n+1)]
        [ls.append(i) for i in range(n-1 , 1 , -1)]

        # print(ls)
        return ls[time % len(ls)]
