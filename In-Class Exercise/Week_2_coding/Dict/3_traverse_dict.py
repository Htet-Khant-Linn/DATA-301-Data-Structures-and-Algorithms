# Traversing Through a Dictionary

myDict = {'name': 'Si Thu', 'age': 32, 'address':'Bangkok'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)