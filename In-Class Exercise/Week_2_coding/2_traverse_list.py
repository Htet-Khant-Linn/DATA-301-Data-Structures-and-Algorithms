shoppingList = ['Milk', 'Cheese', 'Butter']

print(shoppingList[2])

print('Milk' in shoppingList)

print('Fruits' in shoppingList)

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"*"
    print(shoppingList[i])

empty = []
for i in empty:
    print('I am empty')