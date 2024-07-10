# https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for op in logs : 
            if stack and op=='../' :
                stack.pop()
            elif op=='./' : 
                pass 
            elif op!='./' and op!='../': 
                stack.append(op)
            # print(stack )

        return len(stack)
