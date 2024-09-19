# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr , mx) : 
            nonlocal res
            if not curr : 
                return 
            if curr.val>=mx : 
                # print(curr.val , mx , 'valid leaf')
                res += 1
            dfs(curr.right , max(curr.val, mx) )
            dfs(curr.left , max(curr.val, mx))
        dfs(root , root.val)
        return res
