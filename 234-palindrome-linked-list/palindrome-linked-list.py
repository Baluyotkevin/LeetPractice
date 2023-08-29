# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        trial = []
        curr = head
        prev = None
        i = 0
        while curr:
            trial.append(curr.val)
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        while prev:
            if prev.val is not trial[i]:
                return False
            i+=1
            prev = prev.next
        return True
        # print(trial)
        # while prev and head:
        #     if head is not prev:
        #         return False
        #     head = head.next
        #     prev = prev.next
        # return True
        
        