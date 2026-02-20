# Tuples vs Lists

Lists1 = [0,1,2,3,4,5,6,7]
print(Lists1)
Lists1[0] = 99
print(Lists1)

# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')

# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')

# print(init_tuple_a == init_tuple_b)

init_tuple = [(0,1), (1,2), (2,3)]

result = sum(n*m for m,n in init_tuple)

print(result)