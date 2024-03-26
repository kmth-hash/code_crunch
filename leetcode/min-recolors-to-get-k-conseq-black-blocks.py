# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = len(blocks)
        start = 0

        for i in range(len(blocks)):

            if i-start+1 == k:
                # print(start , i+1 ,blocks[start : i+1] ,blocks[start : i+1].count('W') )
                if blocks[start : i+1].count('W')<count : 
                    count = blocks[start : i+1].count('W')
                start += 1
        return count
