class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " <-> "
            current = current.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current  = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def reverse_tranverse(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            index += 1
            current = current.next
        return "Item Not Found"

    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None

        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


newDoublyLinkedList = DoublyLinkedList()
newDoublyLinkedList.append(10)
newDoublyLinkedList.append(20)
newDoublyLinkedList.append(30)
print(newDoublyLinkedList)
newDoublyLinkedList.traverse()
print()
newDoublyLinkedList.reverse_tranverse()
newDoublyLinkedList.search(20)
newDoublyLinkedList.search(40)
newDoublyLinkedList.insert(1, 200)
newDoublyLinkedList.append(100)
print(newDoublyLinkedList)
newDoublyLinkedList.pop_first()
print(newDoublyLinkedList)

newDoublyLinkedList.pop()
print(newDoublyLinkedList)
