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

preOrderTraversal(newBT)

def countNodes(rootNode):
    if not rootNode:
        return 0
    return 1 + countNodes(rootNode.leftChild) + countNodes(rootNode.rightChild)

print(countNodes(newBT))


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBT)


def heightOfTree(rootNode):
    if not rootNode:
        return -1
    return 1 + max(heightOfTree(rootNode.leftChild), heightOfTree(rootNode.rightChild))

print(heightOfTree(newBT))


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBT)


def countleaves(rootNode):
    if rootNode is None:
        return 0
    isleaf = rootNode.leftChild is None and rootNode.rightChild is None
    if isleaf:
        return 1
    
    left = countleaves(rootNode.leftChild)
    right = countleaves(rootNode.rightChild)

    return left + right

print(countleaves(newBT))