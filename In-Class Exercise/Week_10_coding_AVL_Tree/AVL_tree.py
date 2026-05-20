import queue_linked_list as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOderTraversal(rootNode):
    if not rootNode:
        return
    inOderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOderTraversal(rootNode.rightChild)

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
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, nodeValue):
    if rootNode is None:
        print("The value not found!")
        return
    
    # Case 1
    if rootNode.data == nodeValue:
        print("The value is found!")

    # Case 2 - If the nodeValue is smaller then go to the left subtree
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            print("The value not found!")
        elif rootNode.leftChild.data == nodeValue:
            print("The value is found!")
        else:
            searchNode(rootNode.leftChild, nodeValue)

    # Case 3 - If the nodeValue is greater then go right subtree
    else:
        if rootNode.rightChild is None:
            print("The value not found!")
        elif rootNode.righthild.data == nodeValue:
            print("The value is found!")
        else:
            searchNode(rootNode.rightChild, nodeValue)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild) # > +1 mean too many left and < -1 mean too many right

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data: # nodeValue is smaller, go to the left side
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else: 
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))

    balance = getBalance(rootNode)

    if balance > 1 and nodeValue < rootNode.leftChild.data: # LL condition
        return rightRotate(rootNode)

    if balance > 1 and nodeValue > rootNode.leftChild.data: # LR condition 
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    if balance < -1 and nodeValue > rootNode.rightChild.data: # RR condition
        return leftRotate(rootNode)
    
    if balance < -1 and nodeValue < rootNode.rightChild.data: # RL condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        leftRotate(rootNode)

    return rootNode


newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)

# levelOrderTraversal(newAVL)

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild) # The smallest value always left side.

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data: # If smaller, go left
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data: # If greater, go right
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else: # found the node
        # Case 1 (leaf or one child)
        # Only right Child exist
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        # Only left Child exist
        elif rootNode.rightChld is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # node has two children
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    balance = getBalance(rootNode)

    if balance > 1 and getBalance(rootNode.leftChild) >= 0: # LL condition
        return rightRotate(rootNode)
    
    if balance > 1 and getBalance(rootNode.leftChild) < 0 : # LR condtion
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    
    if balance < -1 and getBalance(rootNode.rightChild) <= 0: # RR condition
        return leftRotate(rootNode)
    
    if balance < -1 and getBalance(rootNode.rightChild) > 0: # RL condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode

# newAVL = deleteNode(newAVL, 15)
# levelOrderTraversal(newAVL)

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL tree has been successfully deleted."

print(deleteAVL(newAVL))