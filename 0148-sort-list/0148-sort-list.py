# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        sortt=[]
        temp=head
        while temp is not None:
            sortt.append(temp.val)
            temp=temp.next
        sortt.sort()
        temp=head
        index=0
        while temp is not None:
            temp.val=sortt[index]
            index+=1
            temp=temp.next
        return head

        