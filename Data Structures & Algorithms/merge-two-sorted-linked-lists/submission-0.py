# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        output_head = ListNode(None)
        output_list = output_head 
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                # print("p1",p1.val)
                output_list.next =  ListNode(p1.val)
                p1 = p1.next
            else:
                # print("p2",p2.val)
                output_list.next = ListNode(p2.val)
                p2 = p2.next

            output_list = output_list.next
        
        if p1:
            output_list.next = p1
        else:
            output_list.next = p2

        return output_head.next
        



        