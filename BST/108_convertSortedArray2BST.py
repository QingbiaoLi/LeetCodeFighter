# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def buildBST(left, right):
            if left > right: return None

            middle = left + (right - left) // 2

            root = TreeNode(nums[middle])
            root.left = buildBST(left, middle - 1)
            root.right = buildBST(middle + 1, right)
            return root

        return buildBST(0, len(nums) - 1)

