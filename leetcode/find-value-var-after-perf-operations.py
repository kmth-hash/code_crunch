
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        x = operations.count('++X')+ operations.count('X++')-operations.count('--X')-operations.count('X--')
        
        print(x)
        return x