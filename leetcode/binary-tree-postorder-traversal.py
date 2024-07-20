# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self,root,ls):
        if root == None:
            return ls
        else:
            self.traversal(root.left, ls)
            self.traversal(root.right, ls)
            ls.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        self.traversal(root, ls)
        return ls
