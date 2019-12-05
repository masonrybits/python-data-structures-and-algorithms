def binary_search(lst, val):
  first = 0
  last = len(lst)

  while not last <= first:
    mid = (first + last) // 2

    if val > lst[mid]:
      first = mid + 1
    elif val < lst[mid]:
      last = mid
    else:
      return mid
  return -1
