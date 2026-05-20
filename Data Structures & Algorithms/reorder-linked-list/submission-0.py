# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        size = 0
        while curr:
            stack.append(curr)
            curr = curr.next
            size += 1

        curr = head

        for _ in range(size // 2):
            friend = stack.pop()
            friend.next = curr.next
            curr.next = friend
            curr = friend.next
        curr.next = None