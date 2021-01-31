# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right: return targetSum == root.val

        new_sum = targetSum - root.val

        return self.hasPathSum(root.left, new_sum) or self.hasPathSum(root.right, new_sum)
