import queue_linked_list as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drink")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBT)

# def countNodes(rootNode):
#     if not rootNode:
#         return 0
#     return 1 + countNodes(rootNode.leftChild) + countNodes(rootNode.rightChild)

# # print(countNodes(newBT))

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBT)

# def heightOfTree(rootNode):
#     if not rootNode:
#         return -1
#     return 1 + max(heightOfTree(rootNode.leftChild), heightOfTree(rootNode.rightChild))

# # print(heightOfTree(newBT))

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# postOrderTraversal(newBT)

# def countLeaves(rootNodes):
#     if rootNodes is None:
#         return 0
    
#     isleaf = rootNodes.leftChild is None and rootNodes.rightChild is None
#     if isleaf:
#         return 1
    
#     left = countLeaves(rootNodes.leftChild)
#     right = countLeaves(rootNodes.rightChild)

#     return left + right

# print(countLeaves(newBT))

# Algorithms
# Put rootNode in Queue
# Repeat until empty:
#   Remove from Queue
#   Print it
#   Add left child
#   Add right child
 
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(newBT)

# Put root in queue
# While queue not empty:
#   Remove node
#   Check value
#   Add left Child
#   Add right Child
# If found -> return "Success"
# If finished -> return "Not Found!"


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not Found!"


# print(searchBT(newBT, "Cold"))

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee

# Use Queue
# Traverse level by level
# Find first empty spot
# Insert

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        return newNode
    
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)

    while not customQueue.is_empty():
        root = customQueue.dequeue().value

        if root.leftChild is None:
            root.leftChild = newNode
            return "Successfully Inserted"
        else:
            customQueue.enqueue(root.leftChild)

        if root.rightChild is None:
            root.rightChild = newNode
            return "Successfully Inserted"
        else:
            customQueue.enqueue(root.rightChild)

newNode = TreeNode("Cola")
insertNodeBT(newBT, newNode)
# levelOrderTraversal(newBT)

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()

            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
    
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)

def deleteDeepestNode(rootNode, deleteNode):
    if not rootNode:
        return
    
    customQueue = queue.Queue()
    customQueue.enqueue(rootNode)

    while not customQueue.is_empty():
        root = customQueue.dequeue().value

        if root.leftChild:
            if root.leftChild is deleteNode:
                root.leftChild = None
                return
            else:
                customQueue.enqueue(root.leftChild)
        
        if root.rightChild:
            if root.rightChild is deleteNode:
                root.rightChild = None
                return
            else:
                customQueue.enqueue(root.rightChild)


# deleteNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, deleteNode)
# levelOrderTraversal(newBT)

# def deleteNodeBT(rootNode, node):
#     if not rootNode:
#         return 'The BT does not exist'
    
#     customQueue = queue.Queue()
#     customQueue.enqueue(rootNode)

#     while not customQueue.is_empty():
#         root = customQueue.dequeue().value

#         if root.data == node:
#             deepestNode = getDeepestNode(rootNode)
#             root.data = deepestNode.data
#             deleteDeepestNode(rootNode, deepestNode)
#             return 'The node has been successfully deleted'
        
#         if root.leftChild is not None:
#             customQueue.enqueue(root.leftChild)

#         if root.rightChild is not None:
#             customQueue.enqueue(root.rightChild)

#     return "Failed to delete"

# # print(deleteNodeBT(newBT, "Hot"))
# # levelOrderTraversal(newBT)

# def deleteBT(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "The BT has been successfully deleted"

# print(deleteBT(newBT))
# levelOrderTraversal(newBT)
        