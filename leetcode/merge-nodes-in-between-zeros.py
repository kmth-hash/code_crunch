# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/?envType=daily-question&envId=2024-07-04

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = None 
        temp = ListNode(-1)
        newNode = temp 

        while head : 
            if head.val==0 : 
                head=head.next 
                sub = 0
                while head and head.val!=0 : 
                    sub += head.val
                    head = head.next 
                if sub!=0:
                    curr = ListNode(sub)
                    temp.next = curr
                    # print(temp)
                    temp = temp.next
                
        return(newNode.next)
        
