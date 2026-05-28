# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def stringify(node: ListNode) -> str:
            if node is None:
                return ""
            else:
                return stringify(node.next) + str(node.val)
            
        s1 = stringify(l1)
        s2 = stringify(l2)
        total = str(int(s1) + int(s2))
        
        prev = None
        head = node = ListNode()

        for i in range(len(total) - 1, -1, -1):
            node.val = int(total[i])
            if prev:
                prev.next = node
            prev = node
            node.next = ListNode()
            node = node.next

        prev.next = None

        return head
            