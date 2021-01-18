# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        if root == None:
            return None

        i, stack = 0, [(root, False)]

        while stack or node:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    i +=1
                    if i == k:
                        return cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorder(root,k)

    def inorder(self, root, k):
        if root is not None: return -1

        x = self.inorder(root.left, k)
        if k == 0: return x
        k -= 1
        if k == 0:
            return root.val
        return self.inorder(root.right, k)


class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack: #When root is not equal to none or stack is not equal to none
            while root: # Search the leftmost node of the tree
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

class Solution3(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = []
        self.helper(root, count)
        return count[k - 1]

    def helper(self, node, count):
        if not node:
            return
        self.helper(node.left, count)
        count.append(node.val)
        self.helper(node.right, count)