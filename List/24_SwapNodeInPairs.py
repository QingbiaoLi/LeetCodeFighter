# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not head: return None
        root = ListNode(0)
        root.next = head

        slow = head  # slower pointer, behind
        fast = head.next  # Faster pointer, in front
        pre = root  # Setting an auxiliary pointer

        while fast:
            slow.next = fast.next
            fast.next = slow
            pre.next = fast
            pre = slow
            if not slow.next: break
            slow = slow.next
            fast = slow.next

        return root.next