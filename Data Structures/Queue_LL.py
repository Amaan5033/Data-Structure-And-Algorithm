

# # Queue using Linked List


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next 
class Queue:
    def __init__(self):
        self.LinkedList=LinkedList()

    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        values=" ".join(values)
        return values

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False




    def enqueue(self,value):
        newNode=Node(value)
        if self.LinkedList.head==None:
            self.LinkedList.head=newNode
            self.LinkedList.tail=newNode
        else:
            self.LinkedList.tail.next=newNode       
            self.LinkedList.tail=newNode
        return "EnQueue Successfull!!!"


    def dequeue(self):
        if self.isEmpty():
            return "The list is empty"
        else:
            tempNode=self.LinkedList.head
            if self.LinkedList.head==self.LinkedList.tail:
                self.LinkedList.head=None
                self.LinkedList.tail=None
            else:
                self.LinkedList.head=self.LinkedList.head.next
            return tempNode
            
    


    def peek(self):
        if self.isEmpty():
            return "there is no element in the list"
        else:
            return self.LinkedList.head.value


    def deleteAll(self):
        self.LinkedList.head=None
        self.LinkedList.tail=None




# customQueue=Queue()

# # print(customQueue.isEmpty())

# # print(customQueue.enqueue(1))
# # print(customQueue.enqueue(2))
# # print(customQueue.enqueue(3))
# # print(customQueue.enqueue(4))
# # # print(customQueue.dequeue())    
# # # print(customQueue.dequeue())
# # print(customQueue.peek())
# # customQueue.deleteAll()
# # print(customQueue.isEmpty())
# # print(customQueue)


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
    
#     def __str__(self):
#         return str(self.value)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Queue:
#     def __init__(self):
#         self.linkedList = LinkedList()
    
#     def __str__(self):
#         values = [str(x) for x in self.linkedList]
#         return ' '.join(values)
    
#     def enqueue(self, value):
#         newNode = Node(value)
#         if self.linkedList.head == None:
#             self.linkedList.head = newNode
#             self.linkedList.tail = newNode
#         else:
#             self.linkedList.tail.next = newNode
#             self.linkedList.tail = newNode
    
#     def isEmpty(self):
#         if self.linkedList.head == None:
#             return True
#         else:
#             return False
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "There is not any node in the Queue"
#         else:
#             tempNode = self.linkedList.head
#             if self.linkedList.head == self.linkedList.tail:
#                 self.linkedList.head = None
#                 self.linkedList.tail = None
#             else:
#                 self.linkedList.head = self.linkedList.head.next
#             return tempNode
    
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any node in the Queue"
#         else:
#             return self.linkedList.head
    
#     def delete(self):
#         self.linkedList.head = None
#         self.linkedList.tail = None




# custQueue = Queue()
# custQueue.enqueue(1)
# custQueue.enqueue(2)
# custQueue.enqueue(3)
# print(custQueue)
# print(custQueue.peek())
# print(custQueue)




