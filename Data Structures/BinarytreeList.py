# Binary Tree using List 

# -First cell will remain empty 
# -Left Child=cell[2x]
# -Right Child = cell[2x+1]

# where x is the index of rootnode cell


# Creation of Binary Tree

class BinaryTree:
    def __init__(self,size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size
# O(1),O(n)


# insert a value in Binary tree
    def insert(self,nodeValue):
        if self.lastUsedIndex+1==self.maxSize:
            return "The Binary tree is full"
        self.customList[self.lastUsedIndex+1]=nodeValue
        self.lastUsedIndex+=1
        return "The value is successfully inserted"


    def searchNode(self,nodevalue):
        if self.lastUsedIndex==0:
            return "The Binary Tree is Empty"
        else:
            for i in range(len(self.customList)):
                if self.customList[i+1]==None:
                    break
                elif self.customList[i]==nodevalue:
                    return "The value is present in Binary Tree"
        return "The value is not present on the list"

# -Left Child=cell[2x]
# -Right Child = cell[2x+1]

    def preorderTraversal(self,index):
        if self.lastUsedIndex==0:
            return "The binary Tree is Empty"
        if index>self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preorderTraversal(index*2)
        self.preorderTraversal(index*2+1)

# Blank return statement can be used to transfer the 
# control back to the calling function 
      

# Inorder traversal

    def inorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return 
        self.inorderTraversal(index*2)
        print(self.customList[index])
        self.inorderTraversal(index*2+1)


    def postorderTraversal(self,index):
        if index>self.lastUsedIndex:
            return 
        self.postorderTraversal(index*2)
        self.postorderTraversal(index*2+1)
        print(self.customList[index])        
# O(n),O(n)


    def levelordertraversal2(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])


    def deleteNode(self,nodeValue):
        for i in range(1,self.lastUsedIndex):
            if self.customList[i]==nodeValue:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "The node is deleted"


    def deleteEntire(self):
        self.customList=None
        return "The binary is deleted"
        

        



newBT =BinaryTree(8)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")
newBT.insert("Fanta")
newBT.insert("Cola")
# print(newBT.searchNode("fanta"))
newBT.deleteEntire()
newBT.levelordertraversal2(1)