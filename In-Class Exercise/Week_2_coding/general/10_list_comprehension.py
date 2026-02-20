myList = [1,2,3]
new_list = []
print(myList)

for i in myList:
    multiply_by_2 = i * 2
    new_list.append(multiply_by_2)

print(new_list)

list_comprehension = [x*2 for x in myList]
print(list_comprehension)

word = 'Apple'
word_list_comprehension = [letter for letter in word]
print(word_list_comprehension)