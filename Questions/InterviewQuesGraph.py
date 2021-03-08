# Question No 1

# Given a directed Graph and two nodes (S and E) design 
# an algorithm to find out whether there is a route
# from S to E

# Solution

# Create function with Start and End Node
# Create Queue and enqueue start Node to it
# Find all the neighbours of just enqueued Node and enqueue
# them into the Queue
# Repeat this process until the end of elements in Graph
# If During the above process at some point in time
# we encounter the destination node we return True
# Mark visited node as Visited

# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
    
#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)
    
#     def checkRoute(self, startNode, endNode):
#         visited=[]
#         queue=[startNode]
#         path=False
#         while queue:
#             popQueue=queue.pop(0)
#             if popQueue==endNode:
#                 path=True
#             if popQueue not in visited:
#                 for i in self.gdict[popQueue]:
#                     queue.append(i)
#                 visited.append(popQueue)
#         return path

    
# # O(n^2)


# customDict={"a":["c","d","b"],
#             "b":["j"],
#             "c":["g"],
#             "d":[],
#             "e":["f","a"],
#             "f":["i"],
#             "g":["d","h"],
#             "h":[],
#             "i":[],
#             "j":[]
# }

# g=Graph(customDict)
# print(g.checkRoute("a","e"))



# Question 2

# Given a sorted array with unique integers elements
# write an algorithm to create a binary search tree 
# with minimal height



# Minimal Binary Search Tree

# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# # Here we have print binary search tree in a unique way by using code from stack overflow

#     def display(self):
#         lines, *_ = self._display_aux()
#         for line in lines:
#             print(line)

#     def _display_aux(self):
#         """Returns list of strings, width, height, and horizontal coordinate of the root."""
#         # No child.
#         if self.right is None and self.left is None:
#             line = '%s' % self.data
#             width = len(line)
#             height = 1
#             middle = width // 2
#             return [line], width, height, middle

#         # Only left child.
#         if self.right is None:
#             lines, n, p, x = self.left._display_aux()
#             s = '%s' % self.data
#             u = len(s)
#             first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
#             second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
#             shifted_lines = [line + u * ' ' for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

#         # Only right child.
#         if self.left is None:
#             lines, n, p, x = self.right._display_aux()
#             s = '%s' % self.data
#             u = len(s)
#             first_line = s + x * '_' + (n - x) * ' '
#             second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
#             shifted_lines = [u * ' ' + line for line in lines]
#             return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

#         # Two children.
#         left, n, p, x = self.left._display_aux()
#         right, m, q, y = self.right._display_aux()
#         s = '%s' % self.data
#         u = len(s)
#         first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
#         second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
#         if p < q:
#             left += [n * ' '] * (q - p)
#         elif q < p:
#             right += [m * ' '] * (p - q)
#         zipped_lines = zip(left, right)
#         lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
#         return lines, n + m + u, max(p, q) + 2, n + u // 2

# def minimalTree(sortedArray):
#     if not sortedArray:
#         return
#     mid=int((len(sortedArray))/2)

#     root=BSTNode(sortedArray[mid])

#     root.left=minimalTree(sortedArray[:mid])

#     root.right=minimalTree(sortedArray[mid+1:])

#     return root







# sortedArray=[1,2,3,4,5,6,7,8,9]

# bst=BSTNode(sortedArray)

# root=minimalTree(sortedArray)

# root.display()
# expected output


#           5
#          / \
#         3   8
#        /\   /\
#       2 4  7  9
#      /    /
#     1    6



# Question 3 

# Given a binary search tree design an algorithm which 
# creates a linked list of all the nodes at each depth 
# (i.e if you have a tree with depth D, you'll have 
# D linked list )



# List of Depth
# class LinkedList:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
    
#     def add(self, val):
#         if self.next == None:
#             self.next = LinkedList(val)
#         else:
#             self.next.add(val)
#     def __str__(self):
#         return "({val})".format(val = self.val) + str(self.next)

# class BinaryTree:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
    
# def depth(tree):
#     if tree is None:
#         return 0 
#     if tree.left==None and tree.right==None :
#         return 1 
#     else:
#         depthLeft=1+depth(tree.left)
#         depthRight=1+depth(tree.right)

#         if depthLeft>depthRight:
#             return depthLeft
#         else:
#             return depthRight








# def treeToLinkedList(tree, custDict = {}, d = None):
#     if d==None:
#         d=depth(tree)
#     if custDict.get(d)==None:
#         custDict[d]=LinkedList([tree.val])
#     else:
#         custDict[d].add([tree.val])
#         if d==1:
#             return custDict
#     if tree.left!=None:
#         custDict=treeToLinkedList(tree.left,custDict,d-1)
#     if tree.right!=None:
#         custDict=treeToLinkedList(tree.right,custDict,d-1)
#     return custDict

# mainTree=BinaryTree(1)
# two= BinaryTree(2)
# three= BinaryTree(3)
# four= BinaryTree(4)
# five= BinaryTree(5)
# Six= BinaryTree(6)
# Seven= BinaryTree(7)
# mainTree.left=two
# mainTree.right=three 
# two.left=four
# two.right=five
# three.left=Six
# three.right=Seven



# custDict=treeToLinkedList(mainTree)
# for depthlevel,linkedList in custDict.items():
#     print("{0} {1}".format(depthlevel,linkedList))



# Question 4 

# Implement a function to check if a binary tree is balanced.
# for the purposes of this question a balanced tree is defined 
# to be a tree such that the heights of the two subtrees 
# of any node never differ by more than one

# Balanced Tree

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        


def isBalancedHelper(root):
    if root is None:
        return 0
    leftHeight=isBalancedHelper(root.left)
        return -1
    rightHeight=isBalancedHelper(root.right)
    if rightHeight==-1:
        return -1
    if abs(leftHeight-rightHeight)>1:
        return -1
    return max(leftHeight,rightHeight)+1    

def isBalanced(root):
    return isBalancedHelper(root)>-1

    




maintree=Node("N1")
left=Node("N2")
right=Node("N3")
leftleft=Node("N4")
leftright=Node("N5")
rightright=Node("N6")
maintree.left=left
maintree.right=right
left.left=leftleft
left.right=leftright
right.right=rightright

print(isBalanced(maintree))