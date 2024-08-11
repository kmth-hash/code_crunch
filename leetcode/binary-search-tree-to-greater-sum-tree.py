https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = 0
        def inorder(root) : 
            if not root : 
                return None 
            inorder(root.right)
            # print(root.val)
            self.res += root.val
            root.val = self.res
            inorder(root.left)
        inorder(root)
        # print(root)
        return root
