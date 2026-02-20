# Search the element in Tuple

newTuple = ('a', 'b', 'c', 'd', 'e')

def searchTuple(mytuple, target):
    for i in range(0, len(mytuple)):
        if mytuple[i] == target:
            return f"The element is found at {i} index"
    return 'The element is not found!'

print(searchTuple(newTuple, 'x')) # 'c' and 'x'