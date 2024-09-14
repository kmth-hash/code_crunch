# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        

        def traverse(ll , rr ) : 
            if not ll and not rr : 
                return True 
            elif not ll or not rr : 
                return False 
            if ll.val != rr.val : 
                return False             
            if not traverse(ll.left , rr.right) or not traverse(ll.right , rr.left) : 
                return False             
            return True 

        return traverse(root.left , root.right)
