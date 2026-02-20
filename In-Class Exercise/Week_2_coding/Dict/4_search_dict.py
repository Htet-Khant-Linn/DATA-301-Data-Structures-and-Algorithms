# Search through a dictionary

myDict = {'name': 'Si Thu', 'age': 32, 'address':'Bangkok', 'major':'Biomedical'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The values does not exist!'

print(searchDict(myDict, 'Bangkok')) # 'Bangkok'