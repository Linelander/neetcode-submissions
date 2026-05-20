# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        stack = []
        curr = head

        stack.append(dummy)
        while curr:
            stack.append(curr)
            curr = curr.next

        for i in range(n + 1):
            before = stack.pop()

        if before and before.next:
            temp = before.next.next
            before.next = None
            before.next = temp

        return dummy.next