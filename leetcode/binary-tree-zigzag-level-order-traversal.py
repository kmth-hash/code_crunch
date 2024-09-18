# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = [(root,0)]
        res = {}
        if not root : 
            return []

        while levels : 
            curr,itr = levels.pop(-1)
            # print(curr.val , itr)
            res[itr] = res.get(itr , [])
            res[itr].append(curr.val)
            if curr.left : 
                levels.append((curr.left,itr+1))
            if curr.right : 
                levels.append((curr.right,itr+1))
        
        for x,i in enumerate(res.values()) : 
            # print(i,x)
            if x%2==0 : 
                res[x] =i[::-1]

        return res.values()
            
