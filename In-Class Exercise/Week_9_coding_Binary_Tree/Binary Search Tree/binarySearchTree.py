import queue_linked_list as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    # Case 1
    if rootNode.data is None:
        rootNode.data = nodeValue
    
    # Case 2
    elif nodeValue <= rootNode.data: # less than the rootNode, go to the left side
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    
    # Case 3
    else:                             # greater than rootNode, go to the right side
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted!"

newBST = BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# Root -> left -> right
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBST)

# left -> root -> right
def inOderTraversal(rootNode):
    if not rootNode:
        return
    inOderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOderTraversal(rootNode.rightChild)

# inOderTraversal(newBST)

# left -> right -> root
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# postOrderTraversal(newBST)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.is_empty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# levelOrderTraversal(newBST)

def searchNode(rootNode, nodeValue):
    if rootNode is None:
        print("The value not found")
        return
    
    # Case 1
    if rootNode.data == nodeValue:
        print("The value is found!")

    # Case 2
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is None:
            print("The value is not found!")
        elif rootNode.leftChild.data == nodeValue:
            print("The value is found!")
        else:
            searchNode(rootNode.leftChild, nodeValue)

    # Case 3
    else:
        if rootNode.rightChild is None:
            print("The value is not found!")
        elif rootNode.rightChild.data == nodeValue:
            print("The value is found!")
        else:
            searchNode(rootNode.rightChild, nodeValue)

# searchNode(newBST, 120)

def minValueNode(bstNode):
    current = bstNode # Start from the given node
    while (current.leftChild is not None): # The smallest value is always leftmost node
        current = current.leftChild # Move one step to the left
    return current # If there is no left child, return that node

def deleteNode(rootNode, nodeValue):
    if rootNode is None: # Base case and stop recursion
        return rootNode
    if nodeValue < rootNode.data: # If smaller, go left
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue) # Updated subtree to leftChild
    elif nodeValue > rootNode.data: # if greater, go right
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue) # updated subtree to rightChild
    else: # found the node
        # Case 1 and 2 -> leaf node or one child
        # Only right child is exist
        if rootNode.leftChild is None: # no child or only right child exist
            temp = rootNode.rightChild # save right child in temp
            rootNode = None # remove the current node
            return temp # return the right child 
        # Only left child exist
        if rootNode.rightChild is None: # no child  or only left child exist
            temp = rootNode.leftChild # save left child in temp
            rootNode = None # remove the current node
            return temp # return the left child
        # Case 3 -> node has two children
        temp = minValueNode(rootNode.rightChild) # Find the smallest node in the right subtree
        rootNode.data = temp.data # copy that smallest value into the current node
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data) # delete that node
    return rootNode # return the updated root after deletion


# deleteNode(newBST, 20)
# levelOrderTraversal(newBST)

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted!"

print(deleteBST(newBST))