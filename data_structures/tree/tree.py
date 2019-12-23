class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr=[]):

        node = node or self.root
        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def post_order(self, node=None, arr=[]):
        node = node or self.root
        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)
        return arr

    def in_order(self, node=None, arr=[]):

        node = node or self.root
        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)
        return arr


class BinarySearchTree(BinaryTree):

    def add(self, value):

        if not self.root:
            self.root = None
            return

        node = Node(value)

        if value < self.root.value:
            if not self.root.left:
                self.root.left = node
        else:
            if not self.root.right:
                self.root.right = node

    def contains(self, value, node=None):

        node = node or self.root
        if not self.root:
            return False

        if node.value == value:
            return True

        if value < node.value:
            if node.left:
                return self.contains(value, node.left)
            else:
                return False
        else:
            if node.right:
                return self.contains(value, node.right)
            else:
                return False
