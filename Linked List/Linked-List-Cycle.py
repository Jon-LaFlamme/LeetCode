"""
Difficulty: Easy

Directions: Given a Linked List Head node, determine if a cycle exists in the list:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        positions = set()
        x = head
        while x.next:
            if x.next in positions:
                return True
            else:
                positions.add(x.next)
            x = x.next
        return False