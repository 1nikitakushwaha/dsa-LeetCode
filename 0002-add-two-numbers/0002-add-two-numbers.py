# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        #optimal sol
        dummy=ListNode(0)
        curr=dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            # Get value from l1
            if l1 is not None:
                val1 = l1.val
            else:
                val1 = 0

            # Get value from l2
            if l2 is not None:
                val2 = l2.val
            else:
                val2 = 0

            # Add both values and carry
            total = val1 + val2 + carry

            # Get the digit that we will put in the new node
            digit = total % 10

            # Get carry for the next addition
            carry = total // 10

            # Create new node
            new_node = ListNode(digit)

            # Attach new node to answer list
            curr.next = new_node

            # Move curr
            curr = curr.next

            # Move l1
            if l1 is not None:
                l1 = l1.next

            # Move l2
            if l2 is not None:
                l2 = l2.next

        return dummy.next
        
