# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next, head.next = head.next, prev
            prev, head = head, next
        return prev


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         while head:
#             head.next, prev, head = prev, head, head.next
#         return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def reverse(node: ListNode, prev: ListNode = None):
#             if not node:
#                 return prev
#             next, node.next = node.next, prev
#             return reverse(next, node)
#
#         return reverse(head)
