# https://leetcode.com/problems/merge-in-between-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        newNode = list1        
        curr = newNode
        # print(curr)
        ind = 1
        restOfList1 = None
        while curr : 
            
            # print(curr.val)         
            if ind==a : 
                # print(curr.val,'Found')                
                for i in range(a,b+1):
                    curr.next = curr.next.next
                
                restOfList1 = curr.next
                curr.next = list2   
                # print(restOfList1,curr)
            if curr.next==None : 
                curr.next = restOfList1
                break
            curr = curr.next 
             
            ind += 1   
        return newNode
