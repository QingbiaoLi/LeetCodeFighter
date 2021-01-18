# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack_l1 = []
        stack_l2 = []
        while l1:
            stack_l1.append(l1)
            l1 = l1.next
        while l2:
            stack_l2.append(l2)
            l2 = l2.next
        quotient = 0
        head = None
        while stack_l1 or stack_l2:
            v1 = stack_l1.pop().val if stack_l1 else 0
            v2 = stack_l2.pop().val if stack_l2 else 0
            remainder = v1 + v2
            # Pop the top from both stacks and do calculation to get value
            # and asign the value to new created node.
            # quotient q and remainder r
            quotient, remainder = divmod(quotient + remainder, 10)
            # Create a head node init it as None
            temp = head
            head = ListNode(remainder)
            head.next = temp
        if quotient:
            # We point head’s next pointer to the new created node
            # and update the new node become head node.
            temp = head
            head = ListNode(quotient)
            head.next = temp
        return head