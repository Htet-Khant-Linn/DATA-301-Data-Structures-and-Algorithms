import array

my_array = array.array('i')

my_array_1 = array.array('i', [1,2,3,4,5])

print(my_array)

print(my_array_1)

import numpy as np

np_array = np.array([], dtype = int)
print(np_array)

np_array_1 = np.array([1,2,3,4,5], dtype = int)
print(np_array_1)