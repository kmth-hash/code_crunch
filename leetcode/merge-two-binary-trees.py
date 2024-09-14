# https://leetcode.com/problems/merge-two-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def traverse(t1 , t2 ) : 
            if t1 and t2 : 
                node = TreeNode(t1.val+t2.val)
                node.left = traverse(t1.left , t2.left)
                node.right = traverse(t1.right, t2.right)
                # print(node)
                return node 
            else : 
                return t1 or t2 

        return traverse(root1 , root2)
        # return root1
