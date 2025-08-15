import numpy as np

arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

# row insert
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=0)
print(new_arr_2d)

# column insert
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=1)
print(new_arr_2d)

# flatten array
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=None)
print(new_arr_2d)