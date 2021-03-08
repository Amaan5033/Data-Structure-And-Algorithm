
from random import randint

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

# make this node printable
    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self,values=None):
        self.head=None
        self.tail=None

    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

    def __str__(self):
        values=[str(x.value) for x in self] 
        return "->".join(values) 


    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result

    def add(self,value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode 
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail


    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_value,max_value))
        return self

# Basic setup is completed



# Question 1 : Remove duplicate by using temporary buffer
# we can also use iterative approach  
    def removeDublicate(self,LL):
        if LL.head==None:
            return "The list doesnt exists"
        else:
            tempNode=LL.head
            templist={tempNode.value}
            while tempNode.next is not None:
                if tempNode.next.value  not in templist:
                    templist.add(tempNode.next.value)
                    tempNode=tempNode.next 
                else:
                    delNode=tempNode.next
                    tempNode.next=delNode.next
                    # O(n),S(n)
            return LL



# Question 2 : Return Nth to last

    def nthtolast(self,LL,n):
        pointer1=LL.head
        pointer2=LL.head

        for i in range(n):
            if pointer2 is None:
                return None
            else:
                pointer2=pointer2.next

        while pointer2:
            pointer1=pointer1.next
            pointer2=pointer2.next
# O(n),O(1)
        return pointer1



# Question 3 : Partition
# Write a code to partition a linked list around
# a value x, such that all the nodes less than x 
# come before all nodes greater than or equal to x


    def partition(self,LL,x):
        tempNode=LL.head
        LL.tail=tempNode
        while tempNode:
            nextNode=tempNode.next
            tempNode.next=None
            if tempNode.value<x:
                tempNode.next=LL.head
                LL.head=tempNode
                

            else:
                LL.tail.next=tempNode
                LL.tail=tempNode
            tempNode=nextNode

        if LL.tail.next is not None:
            LL.tail.next=None
        return LL




# Question 4 : Sum list


    def sumlist(self,l1,l2):
        n1=l1.head
        n2=l2.head
        carry=0
        ll=LinkedList()

        while n1 or n2:
            result=carry
            if n1:
                result+=n1.value
                n1=n1.next
            if n2:
                result+=n2.value
                n2=n2.next

            ll.add(int(result%10))
            carry=result/10

        return ll
        
       #O(n),O(n) 


    def intersection(self,l1,l2):
        if l1.tail is not l2.tail:
            return "They are not intersecting"
        lenA=len(l1)
        lenB=len(l2)

        shorter=l1 if lenA<lenB else l2
        longer=l2 if lenA<lenB else l1


        diff=len(longer)-len(shorter)

        longerNode=longer.head
        shorterNode=shorter.head

        for i in range(diff):
            longerNode=longerNode.next

        while shorterNode is not longerNode:
            shorterNode=shorterNode.next 
            longerNode=longerNode.next

        return longerNode

# helper addition method
    def addsameNode(self,l1,l2,value):
        tempNode=Node(value)
        l1.tail.next=tempNode
        l1.tail=tempNode

        l2.tail.next=tempNode
        l2.tail=tempNode


customLL=LinkedList()



    
# l1=customLL.generate(3,0,3)
# l2=customLL.generate(3,0,9)
l1=LinkedList()
l1.generate(3,0,10)
# l1.add(7)
# l1.add(1)
# l1.add(6)
l2=LinkedList()
l2.generate(5,0,10)
# l2.add(5)
# l2.add(9)
# l2.add(2)

l1.addsameNode(l1,l2,11)
l2.addsameNode(l1,l2,14)
# print(l1)
# print(l2)

# print(customLL.sumlist(l1,l2))
# customLL.removeDublicate(customLL)
# print(customLL.nthtolast(customLL,5))
# print(customLL.partition(customLL,50))
print(l1)
print(l2)

print(customLL.intersection(l1,l2))