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
        remainder = 0
        ans = []
        while l1 != None or l2 != None or remainder != 0:
            if l1 != None and l2 != None:
                curr = (l1.val + l2.val + remainder) % 10
                remainder = (l1.val + l2.val + remainder) // 10
            elif l1 != None:
                curr = (l1.val + remainder) % 10
                remainder = (l1.val + remainder) // 10
            elif l2 != None:
                curr = (l2.val + remainder) % 10
                remainder = (l2.val + remainder) // 10
            elif remainder != 0:
                curr = remainder % 10
                remainder = 0
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            ans.append(curr)

        node = ListNode(ans[0])
        ans_head = node
        for i in range(1, len(ans)):
            node.next = ListNode(ans[i])
            node = node.next
        return ans_head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        node = result
        temp = 0
        while l1 is not None or l2 is not None or temp > 0:
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
            node.next = ListNode(temp % 10)  # 取個位數
            node = node.next
            temp = temp // 10  # 檢查是否要進位
        return result.next