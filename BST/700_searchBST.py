class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None

        if (val == root.val):
            return root
        elif (val > root.val):
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
