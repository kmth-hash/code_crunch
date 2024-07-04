# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        ls = [] 
        while curr :             
            ls.append(curr.val)
            curr = curr.next
            
        try: 
            ls.pop(-n)
        except : 
            # print('Error')
            pass
        # print(ls)
        curr = ListNode(-1) 
        newNode = curr
        for i in ls : 
            temp = ListNode(i)
            curr.next = temp 
            curr = curr.next
        del curr
        del ls
        return newNode.next
