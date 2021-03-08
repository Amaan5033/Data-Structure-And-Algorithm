

class Node:
    def __init__(self,value=None):
        self.value=value 
        self.next=None
        self.prev=None

class CircularDLL:
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

# creation of Circular Doubly Linked List 


    def createCircularDLL(self,nodeValue):
        node=Node(nodeValue)
        self.head=node
        self.tail=node
        node.next=node
        node.prev=node



# insertion in Circular Doubly Linked List 


    def insertCDLL(self,value,location):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            newNode.next=newNode
            newNode.prev=newNode
            
            # return createCircularDLL(value)
        else:
            if location==0:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.head =newNode

            elif location==1:#adding at the end of list
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.tail=newNode
                
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.prev=tempNode
                newNode.next=tempNode.next
                tempNode.next=newNode
                newNode.next.prev=newNode  

# traversal in circular doubly linked list 

    def traversal(self):
        tempNode=self.head 
        while tempNode:
            print(tempNode.value)
            tempNode=tempNode.next
            if tempNode==self.head:
                break
            
# reverse traversal 

    def reversetraversal(self):
        tempNode=self.tail
        while tempNode:
            print(tempNode.value)
            tempNode=tempNode.prev
            if tempNode==self.tail:
                break


# search for a node in CDLL
    def searchNode(self,nodeValue):
        tempNode=self.head
        while tempNode:
            if tempNode.value==nodeValue:
                return "The node is Present on the list"
            tempNode=tempNode.next
            if tempNode==self.head:
                break
        return "The node doesNot exists"



# deletion of node 

    def deleteNode(self,location):
        if self.head==None:
            print("The list doesn't exists")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None

                else:
                    self.tail.next=self.head
                    self.head=self.head.next
                    self.head.prev=self.tail

            elif location==1:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None

                else:
                    # tempNode=self.head
                    # while tempNode:
                    #     if tempNode.next==self.tail:
                    #         break
                    #     tempNode=tempNode.next
                    # tempNode.next=self.head
                    # self.head.prev=tempNode
                    # self.tail=tempNode
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail 
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next 
                    index+=1
                delNode=tempNode.next
                tempNode.next=delNode.next
                delNode.next.prev=tempNode
                
                    
# delete entire Circular DOUble Linked list

    def entireDelete(self):
        if self.head==None:
            print("The List doesnt exists")
        else:
            self.tail.next=None
            tempNode=self.head
            while tempNode:
                tempNode.prev=None
                tempNode=tempNode.next
            self.head=None
            self.tail=None  

                    



                    



CDLL=CircularDLL()

CDLL.createCircularDLL(1)
CDLL.insertCDLL(2,0)
CDLL.insertCDLL(7,1)
CDLL.insertCDLL(3,1)
CDLL.insertCDLL(6,0)
CDLL.insertCDLL(8,0)
CDLL.insertCDLL(9,2)
CDLL.insertCDLL(11,1)

CDLL.deleteNode(0)
CDLL.deleteNode(1)
CDLL.deleteNode(2)
print([node.value for node in CDLL])

CDLL.entireDelete()
print([node.value for node in CDLL])
CDLL.reversetraversal()
# print(CDLL.searchNode(13))









