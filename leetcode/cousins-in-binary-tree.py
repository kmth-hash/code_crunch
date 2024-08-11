# https://leetcode.com/problems/cousins-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.parents = [-1,-1]
        self.level = [-1,-1]

        def depth(curr , d , p) : 
            if not curr : 
                return None 
            depth(curr.right , d+1 , curr.val)
            if curr.val==x : 
                self.parents[0] = p 
                self.level[0] = d
            elif curr.val==y : 
                self.parents[1] = p
                self.level[1] = d 
            depth(curr.left , d+1, curr.val)
        depth(root , 0, 'root')
        # print(self.level , self.parents)
        if self.parents[0]!=self.parents[1] and -1 not in self.parents : 
            if self.level[0]==self.level[1] and -1 not in self.level : 
                return True
        return False
