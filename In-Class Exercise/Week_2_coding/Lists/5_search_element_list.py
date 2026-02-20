my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def linear_search(int_list, target):
    for i, value in enumerate(int_list):
        if value == target:
            return i
    return "Target not found!"

print(linear_search(my_list, 50))
print(linear_search(my_list, 100))