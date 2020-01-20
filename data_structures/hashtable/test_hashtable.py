from hashtable import HashTable, Node

def test_add():
    hash = HashTable()
    hash.add('cat', 'wendy')
    expected = 1
    actual = hash.size
    assert actual == expected

def test_get():
    hash = HashTable()
    hash.add('cat', 'marvin')
    expected = 'marvin'
    actual = hash.get('cat')
    assert actual == expected

def test_contain_none():
    hash = HashTable()
    hash.add('huamn', 'ting')
    expected = False
    actual = hash.contains('cat')
    assert actual == expected

def test_collision():
    hash = HashTable()
    hash.add('cat', 'marvin')
    hash.add('act', 'cat')
    actual = 2
    expected = hash.size
    assert actual == expected

def test_collision_retrieved():
    hash = HashTable()
    hash.add('cat', 'wendy')
    hash.add('act', 'cat')
    actual = 'cat'
    expected = hash.get('act')
    assert actual == expected

def test_hash():
    hash = HashTable()
    expected = hash.hash('cat')
    actual = 844
    assert actual == expected
