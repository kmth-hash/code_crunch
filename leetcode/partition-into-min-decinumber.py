# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

class Solution:
    def minPartitions(self, n: str) -> int:
        x = 0
        for i in n:
            x = max(int(i) , x)
        return x


