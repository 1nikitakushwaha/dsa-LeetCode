# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp=head
        # stack=[]
        # while temp is not None:
        #     stack.append(temp.val)
        #     temp=temp.next
        # temp=head
        # while temp is not None:
        #     e=stack.pop()
        #     temp.val=e
        #     temp=temp.next
        # return head



        #optimal solution 
        prev=None
        curr=head
        while curr is not None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
