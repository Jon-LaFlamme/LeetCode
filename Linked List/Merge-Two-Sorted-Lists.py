"""
Difficulty: Easy

Directions: Merge Two sorted linked lists into one sorted list

Examples: [1,2,3],[1,2,4] Sol: [1,1,2,2,3,4]
"""

# This solution was bad. I think I was struggling with the annoyance of Python
# not having pointers as a language feature.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases
        if not l1:
            return l2
        elif not l2:
            return l1
    
        mapping = {}
        
        while l1:
            if l1.val in mapping:
                mapping[l1.val] += 1
            else:
                mapping.update({l1.val:1})
            l1 = l1.next
        
        
        while l2:
            if l2.val in mapping:
                mapping[l2.val] += 1
            else:
                mapping.update({l2.val:1})
            l2 = l2.next
            
        res = []
        for k,v in sorted(mapping.items()):
            for ii in range(v):
                res.append(k)
               
        head = None
        for val in res[::-1]: 
            head = ListNode(val,head)
        
        return head

## Solution from @OldCodingFarmer is much better IMO
# iteratively
# def mergeTwoLists1(self, l1, l2):
#     dummy = cur = ListNode(0)
#     while l1 and l2:
#         if l1.val < l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     cur.next = l1 or l2
#     return dummy.next
    
# # recursively    
# def mergeTwoLists2(self, l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l1, l2.next)
#         return l2