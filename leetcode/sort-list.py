# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ls = [] 
        while head : 
            ls.append(head.val )
            head = head.next 
        ls.sort(reverse= True)
        res = None 
        for i in ls : 
            tmp = ListNode(i , res)
            res = tmp 
        return res
