# https://leetcode.com/problems/leaf-similar-trees/description

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        def dfs(curr,res) : 
            # nonlocal res
            if not curr :
                return 
            if not curr.left and not curr.right : 
                res.append(curr.val)
                # print(res)
            dfs(curr.left,res)            
            dfs(curr.right,res)
            # print(res)
            return res
        
        return dfs(root1,[])==dfs(root2,[])
