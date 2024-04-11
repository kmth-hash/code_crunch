# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = []
        while head : 
            ls.append(head.val)
            head = head.next
        res = None 
        for i in ls:
            temp = ListNode(val=i,next=res)
            res = temp
        return res
