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
        
        self.length+= 1

    def is_empty(self):
        return self.length == 0
    
    def dequeue(self):
        if self.is_empty():
            return "There is no node in the QUEUE"
        else:
            popped_node = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                popped_node.next = None
            self.length -= 1
            return popped_node.value
    
    def peek(self):
        if self.is_empty():
            return "There is no node in the QUEUE"
        else:
            return self.head.value
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0


new_queue = Queue()
new_queue.enqueue(10)
new_queue.enqueue(20)
new_queue.enqueue(30)
new_queue.enqueue(40)

new_queue.peek()

new_queue.dequeue()

new_queue.peek()

new_queue.is_empty()

new_queue.peek()

new_queue.delete_all()

new_queue.peek()