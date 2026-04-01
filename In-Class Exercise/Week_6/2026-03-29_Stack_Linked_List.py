class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value
    

    def peek(self):
        if self.top is None:
            return None
        return self.top.value
    
    def is_empty(self):
        return self.length == 0
    
    def delete_all(self):
        self.top = None
        self.length = 0
    
new_stack = Stack()
new_stack.push(10)
new_stack.push(20)
new_stack.push(30)
new_stack.push(40)
print(new_stack.pop())
print(new_stack.peek())
print(new_stack.is_empty())
new_stack.delete_all()
print(new_stack.is_empty())


def reversed_number(number):
    stack = Stack()

    for num in str(number):
        stack.push(num)
    
    result = ""

    while not stack.is_empty():
        result += stack.pop()
    
    return int(result)

print(reversed_number(12345678))