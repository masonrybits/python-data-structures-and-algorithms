from insert_sort import insertion_sort

def test_insertion_sort():
    arr = [5,10,2,14,8]
    expected = [2,5,8,10,14]
    insertion_sort(arr)
    assert arr == expected

def test_insertion_sort_empty():
    arr = []
    expected = []
    insertion_sort(arr)
    assert arr == expected
