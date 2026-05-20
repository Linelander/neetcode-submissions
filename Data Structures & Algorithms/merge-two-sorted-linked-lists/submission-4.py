# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        head = result

        while list1 and list2:
            if list1.val <= list2.val:
                print("1")
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                print("2")
                result.next = list2
                result = result.next
                list2 = list2.next
        
        if list1: result.next = list1
        
        if list2: result.next = list2

        result = head
        result = result.next
        return result
