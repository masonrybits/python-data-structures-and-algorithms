from tree import BinaryTree, BinarySearchTree

def pre_order():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)
    assert pre_order() == [5,10,15]

def in_order():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)
    assert in_order() == [10,5,15]

def post_order():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(10)
    tree.add(15)
    assert post_order() == [10,15,5]


