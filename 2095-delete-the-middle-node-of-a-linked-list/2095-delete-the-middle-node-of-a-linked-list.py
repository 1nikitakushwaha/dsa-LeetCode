# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        count = 0
        temp = head

        while temp is not None:
            count += 1
            temp = temp.next

        middle = count // 2

        temp = head
        prev = None

        for i in range(middle):
            prev = temp
            temp = temp.next

        prev.next = temp.next

        return head