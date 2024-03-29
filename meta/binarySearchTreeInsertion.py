class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print
    root.info,
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.

        # if not self.root:
        #     self.root = Node(val)
        #     return self.root

        # while self.root:

        #     if val <= self.root.info:
        #         if self.root.left==None:
        #             self.root.left = Node
        #         else:
        #             self.root.left = Node(val)
        #     else:
        #         if self.root.right == None:
        #             self.root.right = Node
        #         else:
        #             self.root.right = Node(val)
        # return self.root
        cur = self.root
        if not cur:
            self.root = Node(val)
            return self.root

        while cur:
            if cur.info > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    break

        return self.root


tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.insert(arr[i])

preOrder(tree.root)
