class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.is_empty():
            return "There is no node in the Queue."
        else:
            popped_node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                popped_node.next = None
            self.length -= 1
            return popped_node
        
    def peek(self):
        if self.is_empty():
            return "There is no node in the Queue."
        else:
            return self.head
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0



