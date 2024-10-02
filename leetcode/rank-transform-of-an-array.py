# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-02

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = sorted(set(arr))
        m = {}
        for i in range(len(s)):
            m[s[i]] = i+1
        return [m[i] for i in arr]
