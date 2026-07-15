# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        l1 = list1
        l2 = list2
        while l1.next and l2:
            if l1.next and l1.next.val > l2.val:
                temp = l1.next
                l1.next = l2
                l2 = temp
            l1 = l1.next
        if l2:
            l1.next = l2
        return list1       
