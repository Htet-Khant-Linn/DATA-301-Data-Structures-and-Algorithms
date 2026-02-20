myList = [1,2,3,4,5,6,7]
print(myList)

myList[2] = 33
print(myList)

myList[4] = 55
print(myList)

myList.insert(4, 15)
print(myList)

newList = [11, 12, 13, 14]
myList.append(newList)
print(myList)

newList = [11, 12, 13, 14]
myList.extend(newList)
print(myList)