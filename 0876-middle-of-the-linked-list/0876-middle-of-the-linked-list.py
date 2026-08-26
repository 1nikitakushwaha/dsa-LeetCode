# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #  **brute force solution tc=o(n) sc=o(1)**
        # count=0
        # curr=head

        # while curr!= None:
        #     count+=1
        #     curr=curr.next
        # middle=count//2
        # curr=head
        # for i in range(0,middle):
        #     curr=curr.next
        # return curr

        #OPTINAL SOLUTION
        slow=head
        fast=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow


    