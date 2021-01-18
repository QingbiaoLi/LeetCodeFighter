# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        cur = head
        insert_pos = dummy

        while cur and cur.next:
            next_val = cur.next.val

            if cur.val <= next_val:
                cur = cur.next
                continue

            if insert_pos.next.val > next_val:
                insert_pos = dummy  # reset

            # use the insert position
            while insert_pos.next.val < next_val:
                insert_pos = insert_pos.next  # move pos pointer

            nxt = cur.next
            cur.next = nxt.next
            nxt.next = insert_pos.next
            insert_pos.next = nxt

        return dummy.next