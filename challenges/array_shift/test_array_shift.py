from array_shift import insert_shift_array

import pytest

def test_even():
  expected = [2,4,5,6,8]
  actual = insert_shift_array([2,4,6,8], 5)
  assert actual == expected

def test_odd():
  expected = [4,8,15,16,23,42]
  actual = insert_shift_array([4,8,15,23,42], 16)
  assert actual == expected

def test_should_accept_only_array():
    with pytest.raises(AttributeError):
        insert_shift_array('1',3)

