# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next 
        s = 0
        ln = len(res)-1
        print(res)
        from math import pow
        for i in res : 
            if i==1: 
                s += pow(2,ln)
            ln -= 1
        # print(int(s))
        return int(s)
