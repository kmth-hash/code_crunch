# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)

        curr = ListNode(-1)
        starter = curr
        # for i in nums :
        #     node = ListNode(i)
        #     # print(curr,starter)
        #     curr.next = node 
        #     # print(curr,starter)
            
        #     curr = curr.next

        while head :
            # print(head.val , starter)
            if head.val not in nums :
                node = ListNode(head.val)
                curr.next = node 
                curr = curr.next
            head = head.next
        # print(starter.next)
        return starter.next
        
