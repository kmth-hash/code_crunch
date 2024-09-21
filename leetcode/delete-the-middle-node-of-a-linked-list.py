# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head 
        prev= head
        odd = True

        while True : 
            if not fast.next  : 
                break 
            fast = fast.next 
            if not fast.next : 
                odd = False
                break 
            fast = fast.next 
            prev= slow
            slow = slow.next 
            # print(slow , fast ,sep='::' , end='----->\n')
        if fast==slow : 
            return None
        if prev==slow : 
            return ListNode(prev.val)
        if not odd :
            prev = prev.next
        
        if prev.next and prev.next.next :
            prev.next = prev.next.next
        else : 
            prev.next = None
        return(head)
            
            
