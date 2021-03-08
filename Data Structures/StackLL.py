
# Stack using Linked List



class Node:
    def __init__(self,value=None):
        self.value=value
        self.next =next

class LinkedList:
    def __init__(self):
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()

    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False


    def push(self,value):
        newNode=Node(value)
        newNode.next=self.LinkedList.head
        self.LinkedList.head=newNode

    def pop(self):
        if self.isEmpty():
            return "The list doesnt contain any element"

        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return f"The node value which pops out is {nodeValue}"        
            

    def peek(self):
        if self.isEmpty():
            return "The list doesnt exists"
        else:
            nodeValue=self.LinkedList.head.value
            return f"The peek value of the stack is {nodeValue}"


    def deleteEntireStack(self):
        self.LinkedList.head=None
        return "The Stack is Empty now"

customStack=Stack()

customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack.pop())
print(customStack.peek())
print(customStack)
print(customStack.deleteEntireStack())
print(customStack.isEmpty())








