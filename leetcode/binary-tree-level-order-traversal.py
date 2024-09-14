# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        ln = 0 
        def traverse(curr , dep ) : 
            nonlocal res , ln 
            # print(curr , dep , ln )
            if not curr : 
                return 
            if ln <= dep : 
                res.append([curr.val])
                ln += 1 
            else : 
                res[dep].append(curr.val)
            # print(res , curr.val , dep )
            traverse(curr.left , dep+1)
            traverse(curr.right, dep+1)

        traverse(root , 0)
        return res 
