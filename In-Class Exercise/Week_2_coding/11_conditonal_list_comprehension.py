my_List = [-1, 10, -20, 2, -90, 60, 45, 20]

new_list = [number for number in my_List if number>0]
print(new_list)

new_list_2 = [number*number for number in my_List if number>0]
print(new_list_2)

new_list_3 = [number if number>0 else 0 for number in my_List]
print(new_list_3)

def get_number(number):
    if number > 0:
        return number
    else:
        return 'Negative'
    
new_list_4 = [get_number(number) for number in my_List]
print(new_list_4)

sentence = 'My name is Si Thu'

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

