# Dictionary Methods

myDict = {'name': 'Si Thu', 'age': 32, 'address':'Bangkok', 'major':'Biomedical'}

# myDict.clear()
# print(myDict)

# myDict2 = myDict.copy()
# print(myDict)
# print(myDict2)

newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

print(myDict.items())

print(myDict.keys())

print(myDict.values())

newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)