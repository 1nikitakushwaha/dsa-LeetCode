# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #brute force

        # if head.next is None:
        #     return None

        # count = 0
        # temp = head

        # while temp is not None:
        #     count += 1
        #     temp = temp.next

        # middle = count // 2

        # temp = head
        # prev = None

        # for i in range(middle):
        #     prev = temp
        #     temp = temp.next

        # prev.next = temp.next

        # return head

        #optimal solution baby
        if head.next is None:
            return None
        slow=head
        fast=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
            
        prev.next=slow.next
        return head
            