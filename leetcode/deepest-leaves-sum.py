# https://leetcode.com/problems/deepest-leaves-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
   
class Solution(object):
    maxRes = 0
    maxN = 1
    def traverseNodes(self ,root , n):
        if root!=None : 
            # print(root.val , n)
            if root.left==None and root.right==None:
                if self.maxN < n : 
                    self.maxN = n
                    self.maxRes = root.val
                    print('leaf',root.val , n , self.maxN)
                elif self.maxN == n:
                    self.maxRes += root.val
                    print('leaf',root.val , n , self.maxN)
            self.traverseNodes(root.left , n+1)
            self.traverseNodes(root.right , n+1)
        
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return  0
        self.traverseNodes(root , 1)
        # print(self.maxN , self.maxRes)
        return self.maxRes
