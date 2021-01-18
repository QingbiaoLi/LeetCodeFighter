# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # Use pre_node records the last node traversed
        self.pre_node = TreeNode(float('-inf'))
        # Used to mark two errors
        self.first_error_node = None
        self.second_error_node = None
        self.count = 0

        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            # Compare pre_node value and current node value
            if self.pre_node.val >= root.val and self.first_error_node == None:
                # If pre_ node >=  root.val  It means that there is an error here. Record it
                self.first_error_node = self.pre_node
            if self.pre_node.val >= root.val and self.first_error_node:
                # The second error is marked here, either one or two errors
                self.second_error_node = root
                # It can be terminated if it occurs twice
                self.count += 1
                if self.count == 2:
                    return
            # Maintenance pre_node
            self.pre_node = root
            in_order(root.right)

        in_order(root)
        # Switching node
        self.first_error_node.val, self.second_error_node.val = self.second_error_node.val, self.first_error_node.val



class Solution(object):
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        # Use pre_node records the last node traversed
        self.pre_node = TreeNode(float('-inf'))
        # Used to mark two errors
        self.first_error_node = None
        self.second_error_node = None
        self.count = 0

        def in_order(root):
            if not root:
                return None
            in_order(root.left)
            # Compare pre_node value and current node value
            if self.pre_node.val >= root.val and self.pre_node:
                # If pre_ node >=  root.val  It means that there is an error here. Record it

                if not self.first_error_node:
                    self.first_error_node = self.pre_node
                self.second_error_node = root
            self.pre_node = root
            in_order(root.right)

        in_order(root)
        # Switching node
        self.first_error_node.val, self.second_error_node.val = self.second_error_node.val, self.first_error_node.val
