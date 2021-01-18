# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        We need to check if there is cycle
        -- If there is not cycle return None
        and if there is cycle we set slow pointer to head
        -- If slow pointer and fast pointer are not equal we
        move 1 step for each pointer until the two pointer
        conincide, then we get the node of cycle begining.
        """

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                node = head
                while node != slow:
                    node = node.next
                    slow = slow.next
                return node
        return None



class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        We need to check if there is cycle
        -- If there is not cycle return None
        and if there is cycle we set slow pointer to head
        -- If slow pointer and fast pointer are not equal we
        move 1 step for each pointer until the two pointer
        conincide, then we get the node of cycle begining.
        """

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast