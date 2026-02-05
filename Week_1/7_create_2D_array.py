import numpy as np

# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis = 0) 
# .insert(original array, insert row/col index, new array, col or row)
print(newTwoDArray)


newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis = 0)
print(newTwoDArray)

# Ctrl + /

