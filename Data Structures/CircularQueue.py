# Circular Queue



class CircularQueue:
    def __init__(self,Maxsize):
        self.Maxsize=Maxsize
        # We are initialising an empty list with all values None
        self.items=Maxsize*[None]
        self.start=-1
        self.top=-1
        

    def __str__(self):
        values=[str(x) for x in self.items]
        values=' '.join(values)
        return values


    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.Maxsize:
            return True
        else:
            return False

    def Enqueue(self,value):
        if self.isFull():
            return "We dont have free space to insert value"
        else:
            if self.top+1==self.Maxsize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start =0
            self.items[self.top]=value
            return "The Enqueue is Successfull"


    def Dequeue(self):
        if self.isEmpty():
            return "We dont have any element on our list"

        else:
            # self.items.pop(0)
            # self.start+=1
            # if self.start-1==self.top:
            #     self.top=-1
            #     self.start=-1
            # return "The dequeue is successfull"
            
            firstelement=self.items[self.start]
            start=self.start
            if self.start ==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.Maxsize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstelement

    def peek(self):
        if self.isEmpty():
            return "We dont have any element left"
        else:
            return self.items[self.start]


    def entiredelete(self):
        self.items =self.Maxsize*[None]
        self.start=-1
        self.top=-1
        # self.top=-1
        return self.items

customQueue=CircularQueue(4)
print(customQueue.isFull())
print(customQueue.isEmpty())
print(customQueue.Enqueue(1))
print(customQueue.Enqueue(2))
print(customQueue.Enqueue(3))
print(customQueue.Enqueue(4))
print(customQueue.Dequeue())
# print(customQueue.Dequeue())
# print(customQueue.Dequeue())
# print(customQueue.Dequeue())
# print(customQueue.Dequeue())
# print(customQueue.Dequeue())
print(customQueue.peek())
print(customQueue.entiredelete())
print(customQueue.isEmpty())
# customQueue.Enqueue(3)
print(customQueue)
