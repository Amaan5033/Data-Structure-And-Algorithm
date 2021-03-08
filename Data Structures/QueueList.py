
# Queue with List


class Queue:
    def __init__(self):
        self.items=[]


    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    
    def Enqueue(self,value):
        # if we have too much values, then memory allocation
        # takes time so We have an amortized Time complexity here 
        # And in worst cases the time complexity will become 
        # Quadratic
        self.items.append(value)
        return "The item is successfully entered"


    def Dequeue(self):
        if self.isEmpty():
            return "The Queue doesnt have any elements"
        else:
            return self.items.pop(0)
        # O(n)


    def peek(self):
        if self.isEmpty():
            return "The Queue is Empty"
        else:
            return self.items[0]

    def EntireQueueDelete(self):
        self.items=[]
        return "Your whole list is Fucked up"

if __name__=="__main__":

    customQueue=Queue()
    print(customQueue.isEmpty())    
    customQueue.Enqueue(1)
    customQueue.Enqueue(2)
    customQueue.Enqueue(3)
    
    
    print(customQueue)
    # print(customQueue.Dequeue())
    # print(customQueue.isEmpty())
    print("-"*50)
    # print(customQueue.peek())
    print(customQueue.EntireQueueDelete())
    print(customQueue.isEmpty())
    print(customQueue)








