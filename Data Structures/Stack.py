

# Stack using List

# creating an empty stack

class Stack:
    def __init__(self):
        self.list=[]


    def __str__(self):
         values=self.list.reverse()
         values =[str(x) for x in self.list]
         return "\n".join(values)



# isempty

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False


# push()

    def push(self,value):
        self.list.append(value)

        return self.list 

# pop()
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()


# peek()
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]
            

# delete entire stack 


    def deleteEntire(self):
         self.list = None




customStack=Stack()


customStack.push(1)
customStack.push(2)
customStack.push(3)
# customStack.pop()
# print(customStack.isEmpty())
print(customStack.peek())
# print(customStack.deleteEntire())
print(customStack)







