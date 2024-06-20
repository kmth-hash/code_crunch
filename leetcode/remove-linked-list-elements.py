# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        tmp = ListNode(-1)
        tmp.next= head 
        
        curr = tmp
        # print(curr , tmp , head ,sep='\n\n')
        while curr and curr.next!=None : 
            if curr.next.val != val : 
                curr = curr.next 
            else : 
                curr.next = curr.next.next 
            # print(curr)
        # print(curr , tmp , head ,sep='\n\n')
        return tmp.next
