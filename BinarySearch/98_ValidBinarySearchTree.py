# divide and conquer
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node, min_val, max_val):
        if node is None:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.helper(node.left, min_val, node.val) and self.helper(node.right, node.val, max_val)


# in-order traversal
class Solution2(object):
    def __init__(self):
        self.pre = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root)

    def helper(self, cur):

        if cur is None:
            return True

        if not self.helper(cur.left):
            return False

        if (self.pre is not None and self.pre.val >= cur.val):
            return False

        self.pre = cur

        return self.helper(cur.right)