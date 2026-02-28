'''
Htet Khant Linn

Feb 24, 2026

Week 4

'''

# 1. Node Class - The Building Block

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 2. LinkedList Class - The Container
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


# 3. String Representation (str)
    def __str__(self):
        temp_node = self.head
        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result


# 4. Append - Add to the End
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


# 5. Prepend - Add to the Beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

# 6. Insert - Add at Specific Position
    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node =self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1


# 7. Traverse - Visit All Nodes
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

# 8. Search - Find a Value
    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
# 9. Pop First - Remove from Beginning
    def pop_frist(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

# 10. Pop - Remove from End
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node
    
# 11. Delete All - Clear the List
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList()
print('--- Append ---')
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.prepend(30)
print()
print('--- Insert ---')
new_linked_list.insert(3, 111)
print()

print(new_linked_list)

print('--- Traverse ---')
new_linked_list.traverse()
print()

print('--- Search ---')
print(new_linked_list.search(40))

print('--- Pop First ---')
new_linked_list.pop_frist()
print(new_linked_list)

print('--- Pop First ---')
new_linked_list.pop()
print(new_linked_list)

print('--- Delete All ---')
new_linked_list.delete_all()
print(new_linked_list)