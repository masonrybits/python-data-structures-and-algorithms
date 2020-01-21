from tree import Tree
from tree_intersection import tree_intersection

def test_tree_intersection_number():
    t1 = Tree()
    t1.add(1)
    t1.add(5)
    t1.add(20)
    t1.add(10)
    t1.add(15)
    t2 = Tree()
    t2.add(20)
    t2.add(15)
    t2.add(1)
    t2.add(30)
    t2.add(5)
    actual = tree_intersection(t1,t2)
    expected = {1,5,15,20}
    assert actual == expected

def test_tree_intersection_string():
    t1 = Tree()
    t1.add('dog')
    t1.add('cat')
    t1.add('deer')
    t1.add('rabbit')
    t1.add('bear')
    t2 = Tree()
    t2.add('cat')
    t2.add('monkey')
    t2.add('bat')
    t2.add('bear')
    t2.add('dolphin')
    actual = tree_intersection(t1,t2)
    expected = {'cat','bear'}
    assert actual == expected

def test_tree_intersection_number_unbalanced():
    t1 = Tree()
    t1.add(1)
    t1.add(5)
    t1.add(20)
    t1.add(10)
    t1.add(15)
    t2 = Tree()
    t2.add(20)
    t2.add(15)
    t2.add(1)
    t2.add(30)
    t2.add(5)
    t2.add(15)
    t2.add(40)
    t2.add(20)
    actual = tree_intersection(t1,t2)
    expected = {1,5,15,20}
    assert actual == expected

def test_tree_intersection_other_number():
    t1 = Tree()
    t1.add(0.45)
    t1.add(-5)
    t1.add(-20)
    t1.add(-8.8)
    t1.add(15)
    t2 = Tree()
    t2.add(-20)
    t2.add(8.8)
    t2.add(-1)
    t2.add(0.45)
    t2.add(5)
    actual = tree_intersection(t1,t2)
    expected = {-20, 0.45}
    assert actual == expected
