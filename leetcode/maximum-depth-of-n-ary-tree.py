# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        res = 0
        if not root : 
            return res
        def traverse(curr , depth) :
            nonlocal res
            res = max(res , depth)
            # print(curr.val ,depth)
            if not curr : 
                return None 
            for i in curr.children : 
                traverse(i , depth+1)
        traverse(root , 1)
        return res
