'''
1. Reimplement the Queue data structure with Python List. Queue operations are enqueue, dequeue, peek, is_empty, and delete.

Htet Khant Linn

April 01, 2026


'''

class Queue:
    def __init__(self):
        self.items = []     # create a python list to store values
        self.length = 0

    def __str__(self):
        return str(self.items)  # string representation for the queue

    def enqueue(self, value):
        self.items.append(value)    # add element at the end
        self.length += 1
        return f"Successfully added {value} to the queue."
    
    def dequeue(self):
        if self.is_empty():     # check for empty queue
            return "This is the empty queue."
        else:
            self.length -= 1
            return f"Successfully removed {self.items.pop(0)} from the queue."    # remove the first element from the queue
        
    def peek(self):
        if self.is_empty():     # check for empty queue
            return "This is the empty queue."
        else:
            return self.items[0]    # return the first element

    def is_empty(self):
        return self.length == 0     # check whether the queue is empty
    
    def delete_all(self):
        self.items = []
        self.length = 0
        return "Queue has successfully been cleared."


new_queue_list = Queue()

print("Enqueue")
print(new_queue_list.enqueue(10))
print(new_queue_list.enqueue(20))
print(new_queue_list.enqueue(30))
print(new_queue_list)
print()

print("Dequeue")
print(new_queue_list.dequeue())
print(new_queue_list)
print()

print("Enqueue")
print(new_queue_list.enqueue(40))
print(new_queue_list.enqueue(50))
print(new_queue_list)
print()

print("Peek")
print(new_queue_list.peek())
print()

print(new_queue_list)
print()

print("Check for Empty")
print(new_queue_list.is_empty())
print()

print("Delete All Itmes in the Queue")
print(new_queue_list.delete_all())
print(new_queue_list.is_empty())
print(new_queue_list)