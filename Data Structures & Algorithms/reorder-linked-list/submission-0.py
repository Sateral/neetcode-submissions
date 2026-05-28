# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mapping = dict()

        curr = head
        i = 0
        while curr:
            mapping[i] = (curr)
            i += 1
            curr = curr.next

        n = len(mapping)
        head = node = ListNode()
        i = 0
        t = 0
        switch = True
        while t < n:
            if switch:
                node.next = mapping[i]
                # print(mapping[i].val)
                i += 1
            else:
                node.next = mapping[n - i]
                # print(mapping[n-i].val)
            switch = not switch
            node = node.next
            t += 1
            
        node.next = None