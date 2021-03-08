


class Stack:
    def __init__(self,MaxValue):
        self.MaxValue=MaxValue
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)




# is EMpty

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)==self.MaxValue:
            return True
        else:
            return False


    def push(self,value):
        if self.isFull():
            return "You cant push because size exceeded"
        else:
            self.list.append(value)
            return "The element inserted succesfully"        


    def pop(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list.pop()


    def peek(self):
        if self.isEmpty():
            return "The Stack is Empty"
        else:
            return self.list[len(self.list)-1]
        


customStack=Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
print(customStack.push(1))
customStack.push(2)
customStack.push(3)
customStack.pop()
print(customStack.peek())
print(customStack)
# customStack.pop()

# print(customStack)
