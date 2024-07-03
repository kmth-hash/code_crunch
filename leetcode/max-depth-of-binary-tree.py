# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.m = 0

        def traversal(root , c):
            if root :
                
                self.m = max(self.m , c + 1)
                # print(root.val , c , self.m)
                traversal(root.left , c+1)
                traversal(root.right , c + 1)
        traversal(root , 0)
        return self.m
