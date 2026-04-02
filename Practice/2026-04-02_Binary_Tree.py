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

def countNodes(rootNode):
    if not rootNode:
        return 0
    return 1 + countNodes(rootNode.leftChild) + countNodes(rootNode.rightChild)

def heightOfTree(rootNode):
    if not rootNode:
        return -1
    return 1 + max(heightOfTree(rootNode.leftChild), heightOfTree(rootNode.rightChild))

def countLeaves(rootNode):
    if not rootNode:
        return 0
    isLeaf = rootNode.leftChild is None and rootNode.rightChild is None
    if isLeaf:
        return 1
    left = countLeaves(rootNode.leftChild)
    right = countLeaves(rootNode.rightChild)
    return left + right

print("preOrderTraversal")
preOrderTraversal(newBT)

print("inOrderTraversal")
inOrderTraversal(newBT)

print("postOrderTraversal")
postOrderTraversal(newBT)

print("countNodes")
print(countNodes(newBT))

print("heightOfTree")
print(heightOfTree(newBT))

print("countLeaves")
print(countLeaves(newBT))