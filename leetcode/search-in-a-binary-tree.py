# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        # print(root)
        
        if not root :
            # print('return None')
            return None
        if root.val==val :
            # print('found')
            return root 
        if root.val>val : 
            # print('go left')
            return self.searchBST(root.left ,val)
        else:
            # print('fo right')
            return self.searchBST(root.right,val)
