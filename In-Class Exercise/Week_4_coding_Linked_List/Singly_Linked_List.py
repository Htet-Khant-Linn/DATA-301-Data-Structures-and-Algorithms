class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        # new_node = Node(value)
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def preprend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1

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
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0



# new_node = Node(10)
# print(new_node)

# new_linked_list = LinkedList(10)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.preprend(50)
# print(new_linked_list)

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# # print(new_linked_list)
# new_linked_list.insert(2, 50)
# print(new_linked_list)
# new_linked_list.traverse()

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# print(new_linked_list)
# print(new_linked_list.search(30))

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# print(new_linked_list)
# new_linked_list.pop_first()
# print(new_linked_list)

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# print(new_linked_list)
# new_linked_list.pop()
# print(new_linked_list)

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
new_linked_list.delete_all()
print(new_linked_list.head.value)