from quick_sort import quick_sort

def test_quick_sort():
    arr = [5,10,2,14,8]
    expected = [2,5,8,10,14]
    quick_sort(arr,0,4)
    assert arr == expected

def test_quick_sort_empty():
    arr = []
    expected = []
    quick_sort(arr,0,0)
    assert arr == expected

def test_quick_sort_negative():
    arr = [5,-10,-2,14,8]
    expected = [-10,-2,5,8,14]
    quick_sort(arr,0,4)
    assert arr == expected

def test_quick_sort_one():
    arr = [5]
    expected = [5]
    quick_sort(arr,0,0)
    assert arr == expected

def test_quick_sort_float():
    arr = [1.1,2.2,7.7,4.4]
    expected = [1.1,2.2,4.4,7.7]
    quick_sort(arr,0,3)
    assert arr == expected

def test_quick_sort_duplicates():
    arr = [1,4,2,4,3]
    expected = [1,2,3,4,4]
    quick_sort(arr,0,4)
    assert arr == expected
