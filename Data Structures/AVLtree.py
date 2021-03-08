

# Creation of AVL tree

import Queue_LL as queue 

class AVLNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        self.height=1





def insertNode(rootNode,nodeValue):
    if rootNode is None:
        rootNode.data=nodeValue

    else:
        if rootNode.data>=nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild=AVLNode(nodeValue)
            else:
                insertNode(rootNode.leftChild,nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild=AVLNode(nodeValue)
            else:
                insertNode(rootNode.rightChild,nodeValue)

    return "The Node is successfully inserted"


# insertNode(newAVL,50)
# insertNode(newAVL,90)
# insertNode(newAVL,30)
# insertNode(newAVL,60)
# insertNode(newAVL,80)
# insertNode(newAVL,100)
# insertNode(newAVL,20)
# insertNode(newAVL,10)


def levelOrdertraversal(rootNode):
    if not rootNode:
        return 
    else:
        customQueue=queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root=customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# levelOrdertraversal(newAVL)
        


def searchNode(rootNode,nodeValue):
    if rootNode==None:
        print("The value is not present")
    elif rootNode.data==nodeValue:
        print("The value is found")
    else:
        if rootNode.data>nodeValue:
            if rootNode.leftChild==nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.leftChild,nodeValue)
        if rootNode.data<nodeValue:
            if rootNode.rightChild==nodeValue:
                print("The value is found")
            else:
                searchNode(rootNode.rightChild,nodeValue)

# searchNode(newAVL,5)

# Insert a node in AVL Tree



def getheight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalanceNode):
    newRoot=disbalanceNode.leftChild
    disbalanceNode.leftChild=disbalanceNode.leftChild.rightChild
    newRoot.rightChild=disbalanceNode
    disbalanceNode.height=1+max(getheight(disbalanceNode.leftChild),getheight(disbalanceNode.rightChild))
    newRoot.height=1+max(getheight(newRoot.leftChild),getheight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot=disbalanceNode.rightChild
    disbalanceNode.rightChild=disbalanceNode.rightChild.leftChild
    newRoot.leftChild=disbalanceNode
    disbalanceNode.height=1+max(getheight(disbalanceNode.leftChild),getheight(disbalanceNode.rightChild))
    newRoot.height=1+max(getheight(newRoot.leftChild),getheight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getheight(rootNode.leftChild)-getheight(rootNode.rightChild)



def insertNode(rootNode,nodeValue):
    
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue<rootNode.data:
        rootNode.leftChild=insertNode(rootNode.leftChild,nodeValue)

    else:
        rootNode.rightChild=insertNode(rootNode.rightChild,nodeValue)
    a=rootNode.height
    # print(rootNode.data)    
    # print(rootNode.height)
    rootNode.height=1+max(getheight(rootNode.leftChild),getheight(rootNode.rightChild))
    # print(rootNode.height)

    # print("-"*50)
    balance=getBalance(rootNode)
    # left left
    if balance>1 and nodeValue<rootNode.leftChild.data:
        return rightRotate(rootNode)
    # left right
    if balance>1 and nodeValue>rootNode.leftChild.data:
        rootNode.leftChild=leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # right right
    if balance<-1 and nodeValue>rootNode.rightChild.data:
        return leftRotate(rootNode)
    # right left
    if balance<-1 and nodeValue<rootNode.rightChild.data:
        rootNode.rightChild=rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode
    

# O(logN),O(logN)


# find the successor of the node:

def minValueNode(bstNode):
    current=bstNode
    while (current.leftChild is not None):
        current=current.leftChild

    return current
    

def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return "The tree doesnt Exists"
    else:
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
                temp=rootNode.rightChild
                rootNode=None
                return temp
            temp=minValueNode(rootNode.rightChild)
            rootNode.data=temp.data
            rootNode.rightChild=deleteNode(rootNode.rightChild,temp.data)
        balance=getBalance(rootNode)
        # left left
        if balance>1 and getBalance(rootNode.leftChild)>=0:
            return rightRotate(rootNode)
        # left right
        if balance>1 and getBalance(rootNode.leftChild)<0:
            rootNode.leftChild=leftRotate(rootNode.leftChild)
            return rightRotate(rootNode)
        # right right
        if balance<-1 and getBalance(rootNode.rightChild)<=0:
            return leftRotate(rootNode)
        # right left
        if balance<-1 and getBalance(rootNode.rightChild)>0:
            rootNode.rightChild=rightRotate(rootNode.rightChild)
            return leftRotate(rootNode)
            # rootNode.height=1+max(getheight(rootNode.leftChild),getheight(rootNode.rightChild))
    return rootNode
# O(logn),O(logn)


def deleteEntire(rootNode):
    rootNode.leftChild=None
    rootNode.rightChild=None
    rootNode.data=None
    return "The AVL tree is deleted"



newAVL=AVLNode(30)

newAVL=insertNode(newAVL,25)
newAVL=insertNode(newAVL,35)
newAVL=insertNode(newAVL,20)
newAVL=insertNode(newAVL,15)
newAVL=insertNode(newAVL,5)
newAVL=insertNode(newAVL,10)
newAVL=insertNode(newAVL,50)
newAVL=insertNode(newAVL,60)
newAVL=insertNode(newAVL,70)
newAVL=insertNode(newAVL,65)
# deleteNode(newAVL,65)
deleteEntire(newAVL)
# print(getheight(newAVL))

levelOrdertraversal(newAVL)







