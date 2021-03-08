# Common Operations on Binary Heap

# -Creation of BH
# -Peek top of BH
# -Extract Min/Max
# -Traversal of BH
# -Size of BH
# -Insert Value in BH
# -Delete the Entire BH



class BinaryHeap:
    def __init__(self,size):
        self.customlist=(size+1)*[None]
        self.heapSize =0
        self.maxSize=size+1
# O(1),O(N)



def peekOfHeap(rootNode):
    if rootNode is None:
        return 
    else:
        return rootNode.customlist[1]
#O(1),O(1) 

def sizeofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.heapSize
# O(1),O(1)

def levelorderTraversal(rootNode):
    if rootNode.customlist is None:
        return "The binary tree doesnt exists"
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customlist[i])
# O(n),O(1)


def heapify(rootNode,index,heapType):
    parentindex=int(index/2)
    if index<=1:
        return 
    if heapType=="Min":
        if rootNode.customlist[index]<rootNode.customlist[parentindex]:
            temp=rootNode.customlist[index]
            rootNode.customlist[index]=rootNode.customlist[parentindex]
            rootNode.customlist[parentindex]=temp
        heapify(rootNode,parentindex,heapType)
    elif heapType=="Max":
        if rootNode.customlist[index]>rootNode.customlist[parentindex]:
            temp=rootNode.customlist[index]
            rootNode.customlist[index]=rootNode.customlist[parentindex]
            rootNode.customlist[parentindex]=temp
        heapify(rootNode,parentindex,heapType)
    
    return rootNode
# O(logN),O(logN)

# def heapifyDelete(rootNode,index,heapType):
#     leftChildIndex=int(index*2)
#     rightChildIndex=int(index*2+1)
#     if index>=rootNode.heapSize+1:
#         return
#     if heapType=="Min":
#         if rootNode.customlist[leftChildIndex]<rootNode.customlist[rightChildIndex]:
#             temp=rootNode.customlist[leftChildIndex]
#             rootNode.customlist[leftChildIndex]=rootNode.customlist[1]
#             rootNode.customlist[1]=temp
#             heapify(rootNode,leftChildIndex,heapType)
#         else:
#             rootNode.customlist[leftChildIndex]>rootNode.customlist[rightChildIndex]:
#             temp=rootNode.customlist[rightChildIndex]
#             rootNode.customlist[rightChildIndex]=rootNode.customlist[1]
#             rootNode.customlist[1]=temp
#             heapify(rootNode,leftChildIndex,heapType)
#     if heapType=="Max":


def heapifyDelete(rootNode,index,heapType):
    leftChildIndex=index*2
    rightChildIndex=index*2+1
    swapChild=0

    if rootNode.heapSize<leftChildIndex:
        return
    elif rootNode.heapSize==leftChildIndex:
        if heapType=="Min":
            if rootNode.customlist[index]>rootNode.customlist[leftChildIndex]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index]=rootNode.customlist[leftChildIndex]
                rootNode.customlist[leftChildIndex]=temp
            return 
        if heapType=="Max":
            if rootNode.customlist[index]<rootNode.customlist[leftChildIndex]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index]=rootNode.customlist[leftChildIndex]
                rootNode.customlist[leftChildIndex]=temp
            return
    else:
        if heapType=="Min":
            if rootNode.customlist[leftChildIndex]<rootNode.customlist[rightChildIndex]:
                swapChild=leftChildIndex
            else:
                swapChild=rightChildIndex
            if rootNode.customlist[index]>rootNode.customlist[swapChild]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index]=rootNode.customlist[swapChild]
                rootNode.customlist[swapChild]=temp
        else:
            if rootNode.customlist[leftChildIndex]>rootNode.customlist[rightChildIndex]:
                swapChild=leftChildIndex
            else:
                swapChild=rightChildIndex
            if rootNode.customlist[index]<rootNode.customlist[swapChild]:
                temp=rootNode.customlist[index]
                rootNode.customlist[index]=rootNode.customlist[swapChild]
                rootNode.customlist[swapChild]=temp
        heapifyDelete(rootNode,swapChild,heapType)




def insert(rootNode,value,heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "The Binary heap is full"
    rootNode.customlist[rootNode.heapSize+1]=value
    rootNode.heapSize+=1
    heapify(rootNode,rootNode.heapSize,heapType)
    return "The value is successfully inserted"
# O(logN),O(logN)


def delete(rootNode,heapType):
    if not rootNode:
        return "The rootnode doesnt exists"
    else:
        extractNode=rootNode.customlist[1]
        rootNode.customlist[1]=rootNode.customlist[rootNode.heapSize]
        rootNode.customlist[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyDelete(rootNode,1,heapType)
        return extractNode
# O(logN),O(logN)


def deleteEntire(rootNode):
    rootNode.customlist=None
    return "The Binary heap is successfully deleted"




newBinaryHeap=BinaryHeap(6)
# print(sizeofHeap(newBinaryHeap))
insert(newBinaryHeap,4,"Max")
insert(newBinaryHeap,5,"Max")
insert(newBinaryHeap,2,"Max")
insert(newBinaryHeap,7,"Max")
delete(newBinaryHeap,"Min")
print(deleteEntire(newBinaryHeap))
print(levelorderTraversal(newBinaryHeap))
