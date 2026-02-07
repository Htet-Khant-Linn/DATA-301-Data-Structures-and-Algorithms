import numpy as np

twoDarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDarray)

def accessElement(array, rowIndex, colindex):
    if rowIndex > len(array) or colindex > len(array):
        print("Incorrect Index!")
    else:
        print(array[rowIndex][colindex])

accessElement(twoDarray, 5, 5)