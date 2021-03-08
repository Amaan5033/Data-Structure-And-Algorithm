# Creating a graph 

import QueueList as queue
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

# breadth first Traversal

    def bfs(self,vertex):
        li=[]
        customQueue=queue.Queue()
        customQueue.Enqueue(vertex)
        while not customQueue.isEmpty():
            p=customQueue.Dequeue()
            if p not in li:
                li.append(p)
                for i in range(len(self.gdict[p])):
                    customQueue.Enqueue(self.gdict[p][i])
        return li


# instructor Way
    def bfs1(self,vertex):
        visited=[vertex]
        queue=[vertex]
        while queue:
            devertex=queue.pop(0)
            print(devertex)
            for adjacentvertex in self.gdict[devertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)

# O(V+E),O(V+E)
# v=vertex
# e=edge
# Depth first Traversal

    def dft(self,vertex):
        visited=[vertex]
        stack=[vertex]
        while stack:
            popvertex=stack.pop()
            print(popvertex)
            for adjacentvertex in self.gdict[popvertex]:
                if adjacentvertex not in visited:
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)
# O(V+E,O(V+E)

customDict={"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f"],
            "f":["d","e"]  
                }

graph=Graph(customDict)
print(graph.bfs("c"))
           
  




