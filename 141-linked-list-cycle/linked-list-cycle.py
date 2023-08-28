# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr and curr.next:
            curr = curr.next.next
            head = head.next
            if curr is head:
                return True
        
        return False