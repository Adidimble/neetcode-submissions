# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        head1 = l1
        head2 = l2
        len_l1 = 0
        len_l2 = 0
        while head1:
            len_l1 += 1
            head1 =  head1.next

        while head2:
            len_l2 += 1
            head2 =  head2.next

        head = l1 if len_l1 >= len_l2 else l2

        curr = head
        prev = None

        while curr:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            res = v1 + v2 + carry       
            carry = res//10            
            curr.val = res%10

            prev = curr
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            prev.next = ListNode(carry)

        return head

