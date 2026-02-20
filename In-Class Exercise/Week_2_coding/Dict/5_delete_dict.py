# Delete a element from Dictionary

myDict = {'name': 'Si Thu', 'age': 32, 'address':'Bangkok', 'major':'Biomedical'}
print(myDict)

del myDict['age']
print(myDict)

removed_elements = myDict.popitem()
print(removed_elements)

myDict.clear()
print(myDict)