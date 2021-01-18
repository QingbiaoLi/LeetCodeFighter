# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # init heap
        heap = []
        # init dummy head and cursor
        cursor = dummy = ListNode(0)
        for element in lists:
            # for non-empty linked lists, push the tuple (head node val, head node) onto the heap
            if element:
                heapq.heappush(heap, (element.val, element))
        # due to Python's min heap implementation
        # the heap is now a min heap of head node vals

        while heap:
            # pop the min element (i.e. least node val)
            value, node = heapq.heappop(heap)

            # append the popped value to cursor
            cursor.next = ListNode(value)
            # increment cursor and increment node
            cursor = cursor.next
            node = node.next
            # so that now cursor -> the new node just appended to the tail of the linked list
            # which the dummy head points to
            # and node -> what's remaining of the linked list
            # whose min val was just popped
            # if anything remains, let's do the same thing once again
            # we can see that the top of the heap will always be the min element of all of the
            # remaining lists.
            if node:
                heapq.heappush(heap, (node.val, node))

        return dummy.next


class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        if not lists:
            return None
        left, right = 0, len(lists) - 1
        while right > 0:
            if left >= right:
                left = 0
            else:
                lists[left] = mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]

class Solution3:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = []
        for seq_no, sorted_list in enumerate(lists):
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, seq_no, sorted_list))

        while heap:
            _, seq_no, smallest = heapq.heappop(heap)
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, seq_no, smallest.next))

        return dummy.next