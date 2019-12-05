from array_binary_search import binary_search

def test_one():
  expected = 2
  actual = binary_search([4,8,15,16,23,42], 15)
  assert actual == expected

def test_two():
  expected = -1
  actual = binary_search([11,22,33,44,55,66,77], 90)
  assert actual == expected

def test_strings():
  expected = 3
  actual = binary_search(['a','b','c','d','e'], 'd')
  assert expected == actual
