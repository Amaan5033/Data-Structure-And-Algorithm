


# first step is to create head and tail 


# class Slinkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None


# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None


# singlyLinkedList=Slinkedlist()
# node1=Node(1)
# node2=Node(2)

# singlyLinkedList.head=node1
# singlyLinkedList.head.next=node2
# singlyLinkedList.tail=node2



#creating an insertion method in singly linked list 

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None



class Slinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
# To make our singly linked list printable
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node = node.next
# insert in singly linked list 
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:#adding element to beginning
                newNode.next=self.head
                self.head=newNode
            elif location==1: #Adding element to end
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:#adding element according to index
                tempNode = self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode


    def delSSl(self,location):
        if self.head is None:
            print("The SLL doesnt exists")
        else:
            if location==0:#Deletion of First Node
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location==1:#Deletion of last Node
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    tempNode=self.head
                    while tempNode is not None:
                        if tempNode.next==self.tail:
                            break
                        tempNode=tempNode.next
                    tempNode.next=None
                    self.tail=tempNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index=index+1
                nextNode=tempNode.next
                tempNode.next=nextNode.next



# delete an entire SLL 

    def DeleteSLLALL(self):
        if self.head is None:
            print("The SLL doesnt exists")

        else:
            self.head=None
            self.tail=None


singlyLinkedList=Slinkedlist()

singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,0)
singlyLinkedList.insertSLL(1,4)
singlyLinkedList.insertSLL(1,2)
singlyLinkedList.insertSLL(8,2)
singlyLinkedList.delSSl(2)
singlyLinkedList.delSSl(0)
singlyLinkedList.delSSl(1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.DeleteSLLALL()
print([node.value for node in singlyLinkedList])


