

# Create a Binary Search Tree

import Queue_LL as queue

class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None


newBST=BSTNode(50)


def insertNode(rootNode,nodeValue):
    if not rootNode:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
            if rootNode.leftChild is None:
                rootNode.leftChild=BSTNode(nodeValue)
            else:
                insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
             insertNode(rootNode.rightChild,nodeValue)

    return "The node is successfully inserted"

# O(logN),O(logN)

insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,90)
insertNode(newBST,45)
insertNode(newBST,75)
insertNode(newBST,85)

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


def preorderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.rightChild)

# preorderTraversal(newBST)

# levelordertraversal(newBST)


def searchNode(rootNode,nodeValue):
    
    # if rootNode.data==nodeValue:
    #     return "The value is found"
    # elif rootNode.data>nodeValue:
    #     if rootNode.leftChild.data==nodeValue:
    #         return "The value is found"
    #     else:
    #         searchNode(rootNode.leftChild,nodeValue)
    # else:
    #     if rootNode.rightChild.data==nodeValue:
    #         return "The value is found"
    #     else:
    #         searchNode(rootNode.rightChild,nodeValue)
    # return "The value is not found"


    if rootNode.data==nodeValue:
        print("The value is found")
    elif rootNode.data>nodeValue:
        if rootNode.leftChild.data==nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild.data==nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.rightChild,nodeValue)
    

# searchNode(newBST,100)

# How return statement is working here and always 
# gives me "The value is not found" for every value

# Sample example for understanding

# def test(x):
#     if x > 9 :
#         test(x - 10)
#     else:
#         print('real value',x)
#         return x

# x = int(input())
# y = test(x)
# print('this should be real value',y)

# test(45):
# | test(35):
# | | test(25):
# | | | test(15):
# | | | | test(5):
# | | | | | print('real value',5)
# | | | | | return 5 to test(15)
# | | | | return None to test(25)
# | | | return None to test(35)
# | | return None to test(45)
# | return None



# Delete a node in Binary Search Tree

# -Case 1: The node to be deleted is a leaf Node
# -Case 2: The node has one Child
# -Case 3: The node has two Children

def minValueNode(bstNode):
    current=bstNode
    while (current.leftChild is not None):
        current=current.leftChild

    return current

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue<rootNode.data:
        rootNode.leftChild=deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue>rootNode.data:
        rootNode.rightChild=deleteNode(rootNode.rightChild,nodeValue)
    else:
        if rootNode.leftChild is None:
            temp=rootNode.rightChild
            rootNode=None
            return temp
        if rootNode.rightChild is None:
            temp=rootNode.leftChild
            rootNode=None
            return temp 

        temp=minValueNode(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
    return rootNode

# print(deleteNode(newBST,50))
# levelordertraversal(newBST)



def deleteEntireBST(rootNode):
    rootNode.data=None
    rootNode.leftChild=None
    rootNode.rightChild=None



# deleteEntireBST(newBST)
# levelordertraversal(newBST)


# Big Picture
#                             TC            SC
# -Create BST                   1            1
# -insert a Node BST            logN        logN
# -Traverse BST                 N            N          
# -Search for a Node BST        logN        logN
# -Delete Node from BST         logN        logN
# -Delete Entire BST            1           1



def minValueNode1(bstNode):
    currentNode=bstNode
    while currentNode.leftChild is not None:
        currentNode=currentNode.leftChild

    return currentNode

def deleteNodeBST1(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    else:
        if nodeValue<rootNode.data:
            rootNode.leftChild=deleteNodeBST1(rootNode.leftChild,nodeValue)
        elif nodeValue>rootNode.data:
            rootNode.rightChild=deleteNodeBST1(rootNode.rightChild,nodeValue)
        else:
            if rootNode.leftChild is None:
                temp=rootNode.rightChild
                rootNode=None
                return temp
            if rootNode.rightChild is None:
                temp=rootNode.leftChild
                rootNode=None
                return temp

        temp=minValueNode1(rootNode.rightChild)
        rootNode.data=temp.data
        rootNode.rightChild=deleteNodeBST1(rootNode.rightChild,temp.data)
    return rootNode

deleteNodeBST1(newBST,50)
levelordertraversal(newBST)