# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd 
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 

        while curr.next : 
            temp = ListNode(gcd(curr.val , curr.next.val),curr.next)
            curr.next = temp 
            curr = curr.next.next
        # print(head)
        return head
