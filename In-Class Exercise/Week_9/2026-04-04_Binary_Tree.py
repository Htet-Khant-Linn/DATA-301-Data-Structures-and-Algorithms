import queue_linked_list as  queue

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

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


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

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.is_empty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not Found!"

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee


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
    return "Insertion Failed"

def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        
        while not customQueue.is_empty():
            root = customQueue.dequeue().value

            if root.leftChild is not None:
                customQueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enqueue(root.rightChild)

        deepestNode = root
        return deepestNode


def deleteDeepestNode(rootNode, deleteNode):
    if not rootNode:
        return 
    else:
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

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 'The BT does not exist.'
    
    else:
        customeQueue = queue.Queue()
        customeQueue.enqueue(rootNode)

        while not customeQueue.is_empty():
            root = customeQueue.dequeue().value

            if root.data == node:
                deepestNode = getDeepestNode(rootNode)
                root.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return 'The node has been successfully deleted'
            if root.leftChild is not None:
                customeQueue.enqueue(root.leftChild)

            if root.rightChild is not None:
                customeQueue.enqueue(root.rightChild)
        return "Faile to Delete"


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"


print("preOrderTraversal")
preOrderTraversal(newBT)

print("inOrderTraversal")
inOrderTraversal(newBT)

print("postOrderTraversal")
postOrderTraversal(newBT)

print("levelOrderTraversal")
levelOrderTraversal(newBT)


print("searchBT")
print(searchBT(newBT, "Cold"))

print("searchBT")
print(searchBT(newBT, "Col"))


print("insertNodeBT")
newNode = TreeNode("Cola")
print(insertNodeBT(newBT, newNode))
levelOrderTraversal(newBT)

print("getDeepestNode")
print(getDeepestNode(newBT).data)

print("deleteDeepestNode")
deleteNode = getDeepestNode(newBT)
deleteDeepestNode(newBT, deleteNode)
levelOrderTraversal(newBT)

print("deleteNodeBT")
print(deleteNodeBT(newBT, "Hot"))
levelOrderTraversal(newBT)

print("deleteBT")
print(deleteBT(newBT))
if newBT.data is None:
    print("Tree is empty")
else:
    levelOrderTraversal(newBT)