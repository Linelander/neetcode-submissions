# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(0)
        dummy = result

        while any(lists):
            smallest = (None, float('inf')) # list, smallest val
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val <= smallest[1]:
                    smallest = (i, lists[i].val) # replace based on val

            result.next = lists[smallest[0]]
            result = result.next
            lists[smallest[0]] = lists[smallest[0]].next

        return dummy.next
