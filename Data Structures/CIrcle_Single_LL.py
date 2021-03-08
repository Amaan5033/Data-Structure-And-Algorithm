
# basic requirements to make Circular Singly Linked List

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node 
            if node.next==self.head:
                break 
            node=node.next

# Creating a Circular Singly Linked List 

    def CreatingCircularSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node 


    def insertionCSLL(self,value,location):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            newNode.next=newNode
            
        else:
            if location==0:#Add element to beginning
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:#Add element to the end
                # newNode.next=self.tail.next
                # self.tail.next=newNode
                # self.tail=newNode
                # node =self.head
                # while node:
                #     if node.next==self.head:
                #         break
                #     node=node.next
                newNode.next=self.tail.next#self.head reference
                self.tail.next=newNode
                self.tail=newNode

                
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nextnode=node.next
                node.next=newNode
                newNode.next=nextnode

# Traversing through Circular Single Linked List 

    def traverse(self):
        if self.head is None:
            print("The Circular Linked list is empty")
        else:
            node=self.head
            while node:
                print(node.value)
                node=node.next
                if node==self.tail.next:
                    break              


# Find a node inside CSLL
    def searchNode(self,value):
        if self.head is None:
            print("The CSLL doesnt exists")
        else:
            node=self.head
            while node:
                if node.value==value:
                    return "The value is present on the list"
                node=node.next
                if node==self.tail.next:
                    break
        return "The value is not present on the list"
                
# Deletion in Circular Singly LinkedList


    def deletionCSLL(self,location):
        if self.head is None:
            print("The CSLL doesnt exists")
        else:
            if location==0:#deletion of the first node
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail.next=self.head.next
                    self.head=self.head.next
            elif location==1:#deletion of the last node
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while node:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.tail.next
                    self.tail=node
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                delnode=node.next
                node.next=delnode.next

# deletion of entire CSLL

    def deleteEntireCSLL(self):
        if self.head is None:
            print("The CSLL doesnt exists")
        else:#We need to delete 3 references
            # last node to first node reference
            # head to first node reference
            # tail to last node reference
            self.tail.next=None
            self.head=None
            self.tail=None

circularSLL=CircularSinglyLinkedList()

circularSLL.CreatingCircularSLL(1)
circularSLL.insertionCSLL(2,0)
circularSLL.insertionCSLL(3,0)
circularSLL.insertionCSLL(5,1)
circularSLL.insertionCSLL(7,1)
circularSLL.insertionCSLL(7,2)
# circularSLL.traverse()
# print(circularSLL.searchNode(8))
print([node.value for node in circularSLL])
# circularSLL.deletionCSLL(0)
# circularSLL.deletionCSLL(1)
# circularSLL.deletionCSLL(1)
# circularSLL.deletionCSLL(1)
# circularSLL.deletionCSLL(2)
circularSLL.deleteEntireCSLL()

print([node.value for node in circularSLL])



