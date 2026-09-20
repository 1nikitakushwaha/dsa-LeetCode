# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        prev = None
        curr = head

        while curr is not None:

            if curr.val == val:

                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next

            else:
                prev = curr

            curr = curr.next

        return head