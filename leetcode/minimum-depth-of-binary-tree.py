# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        mn = 99999
        if not root :
            return 0
        def dp(curr , lvl) : 
            nonlocal mn
            if not curr : 
                return 
            
            dp(curr.left , lvl+1)
            dp(curr.right , lvl+1)
            if not curr.left and not curr.right : 
                # print('Leaf : ',curr.val)
                mn = min(mn, lvl)
        dp(root, 1 )
        return mn
