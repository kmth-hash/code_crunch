# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def dp(curr) :
            nonlocal res
            if not curr : 
                return
            for c in curr.children : 
                dp(c)
            res.append(curr.val)
        dp(root)
        return res
