# https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        grid = [[-1]*n for i in range(m)]
        # print(grid)
        top = 0 
        bottom = m-1 
        right = n-1 
        left = 0
        dir = 0
        def getNextval():
            nonlocal head 
            if not head : 
                return -1 
            v = head.val 
            head = head.next
            return v
        # itr = 1
        while top<=bottom and right>=left : 
            if dir==0 : 
                for i in range(left,right+1) : 
                    grid[top][i] = getNextval() 
                    # print(top,i,itr,getNextval())
                    # itr += 1
                top +=1
            elif dir==1 : 
                for i in range(top,bottom+1) : 
                    grid[i][right] = getNextval() 
                    # print(i,right,itr,getNextval())
                    # itr += 1
                right-=1
            elif dir==2 : 
                for i in range(right,left-1,-1):
                    grid[bottom][i] = getNextval() 
                    # print(bottom,i,itr,getNextval())
                    # itr += 1
                bottom -= 1
            else : 
                for i in range(bottom,top-1,-1): 
                    grid[i][left] = getNextval() 
                    # print(i,left,itr,getNextval())
                    # itr += 1
                left += 1
            # itr += 1 
            dir = (dir+1)%4
        return grid
