# Circular Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += " -> "
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head            
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def insert(self, value, index):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break
        
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value  == target:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return "Value not Found!"
    
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def pop_first(self):
        popped_node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

new_circular_linked_list = CircularLinkedList()
new_circular_linked_list.append(10)
new_circular_linked_list.append(20)
new_circular_linked_list.append(30)
new_circular_linked_list.prepend(60)
new_circular_linked_list.insert(100, 3)
print(new_circular_linked_list)
new_circular_linked_list.traverse()
print(new_circular_linked_list.search(20))
print(new_circular_linked_list.search(0))
print(new_circular_linked_list.get(20))
print(new_circular_linked_list.pop_first())
print(new_circular_linked_list)
print(new_circular_linked_list.pop())
print(new_circular_linked_list)
new_circular_linked_list.delete_all()
print(new_circular_linked_list)
