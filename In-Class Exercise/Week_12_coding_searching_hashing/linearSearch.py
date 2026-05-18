
def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


print(linearSearch([20, 50, 90, 30, 40], 50))