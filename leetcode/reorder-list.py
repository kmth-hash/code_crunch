# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        ls = []
        curr = head 
        while curr : 
            ls.append(curr.val)
            curr = curr.next 
        curr = head
        ptr = curr
        # print(curr)
        while ls : 
            if ls : 
                curr.val = ls.pop(0)
                if ls :
                    curr.next = ListNode()
                else : 
                    curr.next = None
                curr = curr.next
            if ls : 
                curr.val = ls.pop(-1)
                if ls :
                    curr.next = ListNode()
                else : 
                    curr.next = None
                curr = curr.next
            # print(ptr)
        
        # print(curr, ptr,head)
