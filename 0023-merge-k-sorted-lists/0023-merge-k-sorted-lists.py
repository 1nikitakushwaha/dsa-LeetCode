# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        result=[]
        for head in lists:
            while head:
               result.append(head.val)
               head=head.next
        result.sort()
        dummy=ListNode(0)
        current=dummy
        for x in result:
            current.next=ListNode(x)
            current=current.next
        return dummy.next
       

