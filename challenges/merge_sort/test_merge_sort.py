from merge_sort import merge_sort

def test_merge_sort():
    arr = [5,10,2,14,8]
    expected = [2,5,8,10,14]
    merge_sort(arr)
    assert arr == expected

def test_merge_sort_empty():
    arr = []
    expected = []
    merge_sort(arr)
    assert arr == expected

def test_merge_sort_negative():
    arr = [5,-10,-2,14,8]
    expected = [-10,-2,5,8,14]
    merge_sort(arr)
    assert arr == expected

def test_merge_sort_one():
    arr = [5]
    expected = [5]
    merge_sort(arr)
    assert arr == expected

def test_merge_sort_float():
    arr = [1.1,2.2,7.7,4.4]
    expected = [1.1,2.2,4.4,7.7]
    merge_sort(arr)
    assert arr == expected

def test_merge_sort_duplicates():
    arr = [1,4,2,4,3]
    expected = [1,2,3,4,4]
    merge_sort(arr)
    assert arr == expected
