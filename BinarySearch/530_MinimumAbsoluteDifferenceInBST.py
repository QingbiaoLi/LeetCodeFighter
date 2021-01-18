class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def inorder(root):
            if not root: return
            inorder(root.left)

            if self.prev is not None: self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val

            inorder(root.right)

        self.prev = None
        self.min_diff = float("inf")
        inorder(root)
        return self.min_diff