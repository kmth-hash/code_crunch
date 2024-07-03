# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ls = []
        def traversal(root ) :
            if root : 
                tempRes = 0
                if root.val>= low and root.val<=high : 
                    ls.append(root.val)
                
                # print(root.val , tempRes)                    
                traversal(root.left )
                traversal(root.right )
                
        traversal(root)
        
        return sum(ls)
        
