
# 1. Node Class (Same as before)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

'''
# One Element inside the node

class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1

new_cslinkedlist = CSLinkedList(10)
print(new_cslinkedlist.head.value)
print(new_cslinkedlist.tail.value)
print(new_cslinkedlist.length)

'''

# 2. CSLinkedList Initialization
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# 3. String Representation (str)
    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            current = current.next
            if current == self.head:
                break
            result += ' - > '
        return result
        


# 4. Append - Add to the End

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

# 5. Prepend - Add to the Beginning

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

# 6. Insert - Add at Specific Position

    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length +=1

# 7. Traverse - Visit All Nodes
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            if current == self.head:
                break

# 8. Search - Find a Value
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            if current == self.head:
                break
            index += 1
        return -1


# 9. Get - Retrieve Value at Index
    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

# 10. Pop First - Remove from Beginning
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

# 11. Pop - Remove from End
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

# 12. Delete All - Clear the List
    def delete_all(self):
        self.tail.next = None   # Break the circle first!
        self.head = None
        self.tail = None
        self.length = 0


# 13. Remove - Homework
    def remove(self, index):
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev_node = self.head
        for _ in range(index-1):
            prev_node = prev_node.next
        removed_node = prev_node.next
        prev_node.next = removed_node.next
        removed_node.next = None
        self.length -= 1
        return removed_node



new_cslinkedlist = CSLinkedList()
new_cslinkedlist.append(10)
new_cslinkedlist.append(20)
new_cslinkedlist.append(30)
new_cslinkedlist.append(40)
new_cslinkedlist.prepend(50)

print('--- Checking ---')
print(new_cslinkedlist.head.value)
print(new_cslinkedlist.tail.value)
print(new_cslinkedlist.length)
print()

print(new_cslinkedlist)
print()

print('--- Insert ---')
new_cslinkedlist.insert(3, 100)
print(new_cslinkedlist)
print()

print('--- Traverse ---')
new_cslinkedlist.traverse()

print('--- Search ---')
print(new_cslinkedlist.search(20))
print(new_cslinkedlist.search(120))

print('--- get ---')
print(new_cslinkedlist.get(2))

print('--- pop first ---')
new_cslinkedlist.pop_first()
print(new_cslinkedlist)

print('--- pop ---')
new_cslinkedlist.pop()
print(new_cslinkedlist)
