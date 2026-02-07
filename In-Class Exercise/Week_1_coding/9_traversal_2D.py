import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

def traverse2Darray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):      # len(array) counts the Rows: len(array[0]) counts the Columns:
                                            # array[0] grabs the first row specifically ([11, 15, 10, 6]). 
                                            # When you take the length of that specific row, you get 4 (the number of items in that row).
            print(array[i][j])

traverse2Darray(twoDArray)