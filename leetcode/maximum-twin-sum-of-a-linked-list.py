# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ls = [] 
        while head : 
            ls.append(head.val)
            head = head.next 
        res = 0
        ln = len(ls)
        for i in range(ln//2) : 
            # print(ls[i]+ls[ln-i-1])
            res= max(ls[i]+ls[ln-i-1],res)

        return res
