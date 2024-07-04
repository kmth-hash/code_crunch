# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head 
        ls = []
              
        while head : 
            ls.append(head.val)
            head = head.next
        if k==0 or len(ls)==0: 
            return curr
        else : 
            k = k%len(ls)
        ls =ls[-k:] + ls[:-k]
        head = ListNode(-1)
        curr = head  
        for i in ls : 
            head.next = ListNode(i)
            head = head.next 
        return curr.next
        
