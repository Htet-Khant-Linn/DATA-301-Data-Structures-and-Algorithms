import math

def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    # print(start, middle, end)
    while not(array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    if array[middle] == value:
        return middle
    else:
        return -1


my_array = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(my_array, 15))

# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S             M                E  (0, 4, 8)
#  S  M       E                      (0, 1, 3)
#         SM  E                      (2, 2, 3)
#            SME                     (3, 3, 3)