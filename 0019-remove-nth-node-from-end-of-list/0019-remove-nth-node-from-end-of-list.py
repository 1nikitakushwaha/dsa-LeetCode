# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        ##brute force!!!!!!## tc=o(n) and sc=o(1) but we want in one traverse
        # length=0
        # temp=head
        # while temp is not None:
        #     length+=1
        #     temp=temp.next
        # if length==n:
        #     new_head=head.next
        #     return new_head
        # pos=length-n
        # count=1
        # temp=head
        # while count<pos:
        #     temp=temp.next
        #     count+=1
        # temp.next=temp.next.next
        # return head
    
    ##optimal solution
        fast=head
        slow=head
        for i in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head

        
