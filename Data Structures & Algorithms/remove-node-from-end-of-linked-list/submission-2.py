# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        idx = N - n
        if idx == 0:
            return head.next

        prev = None
        curr = head
        i = 0
        while i != idx - 1:
            prev = curr
            curr = curr.next
            i += 1
        
        curr.next = curr.next.next

        return head