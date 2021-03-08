

# Creation of Binary tree using Linked List

# -Creation of tree
# -Insertion of Node
# -Deletion of Node
# -Search for a value
# -Traverse all nodes 
# -Deletion of tree
import Queue_LL as queue


class TreeNode:
    def __init__(self,data):
        self.data=data 
        self.leftChild=None
        self.rightChild=None

newBT=TreeNode("Drinks")
leftChild=TreeNode("Cold")
rightChild=TreeNode("Hot")
tea=TreeNode("Tea")
coffee=TreeNode("Coffee")
# cola=TreeNode("Cola")
# fanta=TreeNode("Fanta")
# leftChild.leftChild=cola
# leftChild.rightChild=fanta
rightChild.leftChild=tea
rightChild.rightChild=coffee
newBT.leftChild=leftChild
newBT.rightChild=rightChild


# Traversal of a binary Tree
# Depth first Search
# -Preorder Traversal
# -Inorder Travesal
# -Post order traversal

# Breadth first search
# -Level order traversal

# Preorder traversal

# RootNode-->LeftSubtree-->RightSubtree

# def preorderTraversal(rootNode):
#     if not rootNode:
#         return 
#     print(rootNode.data)
#     preorderTraversal(rootNode.leftChild)
#     preorderTraversal(rootNode.rightChild)
# O(n),O(n)


# preorderTraversal(newBT)


# Inorder Traversal

# leftsubtree-->RootNode-->RightSubtree

# def InorderTraversal(rootNode):
#     if not rootNode:
#         return 
#     else:
#         InorderTraversal(rootNode.leftChild)
#         print(rootNode.data)
#         InorderTraversal(rootNode.rightChild)
# InorderTraversal(newBT)


# PostorderTraversal

# LeftSubtree-->RightSubtree-->RootNode

# def postorderTraversal(rootNode):
#     if rootNode:
#         postorderTraversal(rootNode.leftChild)
#         postorderTraversal(rootNode.rightChild)
#         print(rootNode.data)

# postorderTraversal(newBT)


def levelordertraversal(rootNode):
    if rootNode:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            

# print(levelordertraversal(newBT))        



# Searching for an element

def search(rootNode,nodeValue):
    if rootNode:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==nodeValue:
                return "Successs!!!"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not found"

# print(search(newBT,"Tea"))



# Insert a node in Binary tree 

def insertNodeBT(rootNode,newNode):
    if not rootNode:
        rootNode=newNode
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild=newNode
                return "Successfully inserted"

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild=newNode
                return "Successfully inserted"




# newNode=TreeNode("Cola")
# print(insertNodeBT(newBT,newNode))
# newNode=TreeNode("fanta")
# print(insertNodeBT(newBT,newNode))
# levelordertraversal(newBT)



# Deletion in binaryTree
def deepestNode(rootNode):
    if rootNode:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            # print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepest=root.value
        return deepest


def deletedeepestNode(rootNode,dnode):
    customQueue=queue.Queue()
    customQueue.enqueue(rootNode)
    while not(customQueue.isEmpty()):
        root=customQueue.dequeue()
        if root.value is dnode:
            root.value=None
            return 
        if root.value.rightChild:
            if root.value.rightChild is dnode:
                root.value.rightChild=None
                return 
            else:
                customQueue.enqueue(root.value.rightChild)
        if root.value.leftChild:
            if root.value.leftChild is dnode:
                root.value.leftChild=None
                return 
            else:
                customQueue.enqueue(root.value.leftChild)



def deleteNode(rootNode,node):
    if not rootNode:
        return "The BT doesnt exists"
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==node:
                dnode=deepestNode(rootNode)
                root.value.data=dnode.data
                deletedeepestNode(rootNode,dnode)
                return "The node is deleted"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "failed to delete"
                

# deepNode=deepestNode(newBT)
# deletedeepestNode(newBT,deepNode)
# levelordertraversal(newBT)
# deleteNode(newBT,"Cold")
# levelordertraversal(newBT)



# delete entire Binary Tree


def entireTree(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None
    return "The entire Binary Tree is deleted"

entireTree(newBT)
levelordertraversal(newBT)
