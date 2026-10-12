# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        p2 = head.next
        p1 = head
        p1.next = None

        while p2:
            add = p2.next
            p2.next = p1
            p1=p2
            p2 = add
        
        return p1