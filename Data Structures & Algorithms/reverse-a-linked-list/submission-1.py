# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p1 = head.next
        p2 = head
        p2.next = None
        while p1 != None:
            add = p1.next
            p1.next = p2
            p2 = p1
            p1 = add

        return p2