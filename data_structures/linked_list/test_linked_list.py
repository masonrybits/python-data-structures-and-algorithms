from linked_list import LinkedList

def test_insert():
    ll = LinkedList()
    ll.insert(2)
    expected = '2'
    actual = ll.to_string()
    assert actual == expected

def test_include_empty():
    ll =  LinkedList()
    expected = False
    actual = ll.includes(1)
    assert actual == expected

def test_include_true():
    ll =  LinkedList()
    ll.insert(1)
    expected = True
    actual = ll.includes(1)
    assert actual == expected

def test_include_false():
    ll =  LinkedList()
    ll.insert(1)
    expected = False
    actual = ll.includes(2)
    assert actual == expected

def test_include_three_true():
    ll =  LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    expected = True
    actual = ll.includes(2)
    assert actual == expected

def test_to_string():
    ll =  LinkedList()
    ll.insert(1)
    expected = '1'
    actual = ll.to_string()
    assert actual == expected

def test_to_string_empty():
    ll = LinkedList()
    expected = ''
    actual = ll.to_string()
    assert actual == expected

def test_to_string_two():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    expected = '2 1'
    actual = ll.to_string()
    assert actual == expected

def test_append():
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.insert(1)
    expected = '1 2 3'
    actual = ll.to_string()
    assert actual == expected

def test_insert_before():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.insert_before(3,2)
    expected = '1 2 3'
    actual = ll.to_string()
    assert actual == expected

def test_insert_after():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_after(2,3)
    expected = '1 2 3'
    actual = ll.to_string()
    assert actual == expected

def kth_from_end():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.kth_from_end(1)
    expected = '2'
    actual = ll.to_string()
    assert actual == expected

def kth_from_end_fail():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.kth_from_end(4)
    expected = 'not enough nodes in the list to go back kth term'
    actual = ll.to_string()
    assert actual == expected
