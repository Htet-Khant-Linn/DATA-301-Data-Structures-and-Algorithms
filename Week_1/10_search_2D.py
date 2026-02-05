import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])


def search2DArray(array, target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return "The value is located in row index: " + str(i) + " and col index: " + str(j) + "."
    return "The element is not found!"


print(search2DArray(twoDArray, 15))