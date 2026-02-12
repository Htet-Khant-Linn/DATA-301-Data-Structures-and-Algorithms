myList = list()

while (True):
    input_num = input("Enter a number: ")
    if input_num == 'done':
        break
    value = float(input_num)
    myList.append(value)
average_num = sum(myList)/ len(myList)

print("Average: ", average_num)