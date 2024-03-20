# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy.next
        second = dummy.next
        length = 0
        while first:
            temp = first.val
            first = first.next
            if length % 2 == 0 and second.next is not None:
                second.val = first.val
                second.next.val = temp
            second = second.next
            length += 1
        return dummy.next
