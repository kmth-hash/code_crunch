# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0

        def bfs(curr) : 
            nonlocal res 
            # print(curr.val)
            if not curr : 
                return 
            if curr.left : 
                if not curr.left.left and not curr.left.right : 
                    res += curr.left.val 
                bfs(curr.left)
            bfs(curr.right)

        bfs(root)
        # print(res)
        return res
