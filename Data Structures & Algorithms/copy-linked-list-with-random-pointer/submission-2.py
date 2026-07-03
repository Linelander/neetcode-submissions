"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        d = {}
        curr = head
        prev = None
        while curr:
            nnode = Node(curr.val)
            if prev:
                prev.next = nnode
            prev = nnode

            d[curr] = nnode
            curr = curr.next

        curr = head
        while curr:
            d.get(curr).random = d.get(curr.random)
            curr = curr.next

        return d[head]

