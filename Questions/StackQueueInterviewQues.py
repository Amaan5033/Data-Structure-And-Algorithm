
# Stack and Queues Ininterview Questions


# Question 1 
 
# Describe how you could use a single Python List to 
# implement three stacks



# class MultiStack:
#     def __init__(self,stacksize):
#         self.numberstacks=3
#         self.customList=[0]*(stacksize*self.numberstacks)
#         self.sizes=[0]*self.numberstacks
#         self.stacksize=stacksize

#     def isFull(self,stacknum):
#         if self.sizes[stacknum]==self.stacksize:
#             return True 
#         else:
#             return False

#     def isEmpty(self,stacknum):
#         if self.sizes[stacknum]==0:
#             return True 
#         else:
#             return False



#     def indexoftop(self,stacknum):
#         offset=stacknum*self.stacksize
#         return offset*self.sizes[stacknum]-1


#     def push(self,value,stacknum):
#         if self.isFull(stacknum):
#             return "The stack is full"
#         else:
#             self.sizes[stacknum]+=1
#             self.customList[self.indexoftop(stacknum)]=value


#     def pop(self,stacknum):
#         if self.isEmpty(stacknum):
#             return "This stack is empty"
#         else:
#             value=self.customList(self.indexoftop(stacknum))
#             self.customList[self.indexoftop(stacknum)]=0
#             self.sizes[stacknum]-=1
#             return value


#     def peek(self,stacknum):
#         if self.isEmpty(stacknum):
#             return "The stack is Empty"
#         else:
#             value=self.customList[self.indexoftop(stacknum)]
#             return value


# customStack=MultiStack(6)
# print(customStack.isFull(0))
# print(customStack.isEmpty(1))
# customStack.push(1,0)
# customStack.push(2,0)
# customStack.push(3,2)
# print(customStack.peek(0))






# Question 2

# How would you design a stack which, in addition 
# to push and pop , has a function min which 
# returns the minimum element? Push pop and 
# min should all operate in O(1)


# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None
        

# class LinkedList:
#     def __init__(self):
#         self.head= None
#         self.tail=None

#     def __iter__(self):
#         node=self.head
#         while node:
#             yield node
#             node=node.next

# class Stack:
#     def __init__(self):
#         self.LinkedList=LinkedList()
    

#     def __str__(self):
#         values=[str(x.value) for x in self.LinkedList]
#         return "\n".join(values)

#     def isEmpty(self):
#         if self.LinkedList.head==None:
#             return True
#         else:
#             return False

#     def push(self,value):
#         newNode=Node(value)
#         newNode.next=self.LinkedList.head
#         self.LinkedList.head =newNode
        



#     def pop(self):
#         if self.isEmpty():
#             return "The list is Empty"

#         else:
#             nodevalue=self.LinkedList.head
#             self.LinkedList.head=self.LinkedList.head.next
#             return f"The nodevalue which is popped out is {nodevalue}"


#     def min(self):

#         if newNode.value
   
# customStack=Stack()

# print(customStack.isEmpty())


# customStack.push(1)
# customStack.push(2)
# customStack.push(3)

# print(customStack)
# # print(customStack.isEmpty())
# print("-"*50)
# customStack.pop()
# print(customStack)





# Question 3 


# Imagine a stack of plate if the stack goes too high 
# it might topple.Therefore , in real life we would likely
# start a new Stack when the previous stack exceeds some 
# threshold. Implement a data structure SetOFStacks that 
# mimics this.SetOfStacks should be composed of several
# stacks and should create a new Stack once the previous 
# one exceeds capacity, SetOfSatcks.push() and SetOFStacks.pop()
# should behave identically to a single stack(that is 
# pop() should return the same values as it would if 
# there were just a single stack).

# class PlateStack():
#     def __init__(self,capacity):
#         self.capacity=capacity
#         self.stacks=[]

#     def __str__(self):
#         return self.stacks

#     def push(self,item):
#         if len(self.stacks)>0 and len(self.stacks[-1]) < self.capacity:
#             self.stacks[-1].append(item)
#         else:
#             self.stacks.append([item])


     

#     def pop(self):
#         while len(self.stacks) and len(self.stacks[-1])==0:
#             self.stacks.pop()
#         if len(self.stacks)==0:
#             return None
#         else:
#             return self.stacks[-1].pop()



#     def pop_at(self,stacknum):
#         if stacknum>len(self.stacks):
#             return f"We have only {len(self.stacks)} stacks and you exceed the limit"
#         if len(self.stacks[stacknum])>0:
#             return self.stacks[stacknum].pop()
#         else:
#             return None

#     def totalNumberOfStacks(self):
#         return len(self.stacks)






# customStack=PlateStack(2)
# customStack.push(1)
# customStack.push(2)
# customStack.push(3)
# customStack.push(4)
# customStack.push(5)
# customStack.push(6)
# customStack.push(7)
# customStack.push(7)
# customStack.push(7)
# customStack.push(7)
# # print(customStack.totalNumberOfStacks())
# print(customStack.pop_at(7))




# Question 4

# Implement Queue class which implements a queue using
# two stacks

# class Stack():
#     def __init__(self):
#         self.list=[]

#     def __len__(self):
#         return len(self.list)


#     def push(self,item):
#         self.list.append(item)

#     def pop(self):
#         if len(self.list)==0:
#             return "There is no element in the stack"

#         else:
#             return self.list.pop()

# # We are creating Queue using Two stacks

# class QueueViaStack():
#     def __init__(self):
#         self.inStack=Stack()
#         self.outStack=Stack()

#     def enqueue(self,item):
#         self.inStack.push(item)


#     def dequeue(self):
#         while len(self.inStack):
#             self.outStack.push(self.inStack.pop())
        
#         result=self.outStack.pop()
#         while len(self.outStack):
#             self.inStack.push(self.outStack.pop())
#         return result 


# customQueue=QueueViaStack()

# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# print(customQueue.dequeue())
# # print(customQueue)



# Question 5

# Animal Shelter


class AnimalSheltar():
    def __init__(self):
        self.cats=[]
        self.dogs=[]

    def enqueue(self,animal,type):
        if type=="Cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeuecat(self):
        if len(self.cats)==0:
            return None
        else:
            return self.cats.pop(0)

    def dequeuedog(self):
        if len(self.dogs)==0:
            return None
        else:
            return self.dogs.pop(0)


    def dequeueAny(self):
        if len(self.cats)==0:
            result=self.dogs.pop(0)
        else:
            result=self.cats.pop(0)
        return result


customQueue=AnimalSheltar()
customQueue.enqueue("Dog1","Dog")
customQueue.enqueue("Dog2","Dog")
customQueue.enqueue("Cat1","Cat")
customQueue.enqueue("Dog3","Dog")
customQueue.enqueue("Cat2","Cat")
customQueue.enqueue("Cat3","Cat")

print(customQueue.dequeuedog())
print(customQueue.dequeuecat())







