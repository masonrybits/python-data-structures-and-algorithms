def insert_shift_array(array, value):
  i = len(array)
  if i % 2 == 0:
    mid_index = i // 2
  else:
    mid_index = (i + 1) // 2
  array.insert(mid_index ,value)
  return array
