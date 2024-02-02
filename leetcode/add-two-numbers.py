# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #print(l1,l2)
        s = ''
        while l1.next!=None:
            s += str(l1.val)
            l1 = l1.next
        s += str(l1.val)    
        r = ''
        while l2.next!=None:
            r += str(l2.val)
            l2 = l2.next
        r += str(l2.val)
        res = str(int(s[::-1])+int(r[::-1]))
        print(r,s,res)
        ret_res = [int(i) for i in res]
        l = None
        for i in ret_res:
            l = ListNode(i,next = l)
        print(l)
        
        return l
            
            