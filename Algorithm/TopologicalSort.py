# Sorts given actions in such a way that if there is a
# dependency of one action on another, then the dependent
# action always comes later than its parent action

# For a Directed Acyclic Graph is a linear ordering of 
# vertices such that for every directed edge(u,v), vertex 
# u comes before v in the ordering.


# Creating Graph Class 
# Creating graph using adjency list method 

from collections import defaultdict 

class Graph:
    def __init__(self,numberofVertices):
        self.graph=defaultdict(list)
        self.numberofVertices=numberofVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)


    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)
        stack.insert(0,v)


    def topologicalSort(self):
        visited=[]
        stack=[]

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)
        print(stack)

# O(E+V),O(E+V)
customGraph=Graph(0)
customGraph.addEdge("A","C")
customGraph.addEdge("C","E")
customGraph.addEdge("E","H")
customGraph.addEdge("E","F")
customGraph.addEdge("F","G")
customGraph.addEdge("B","C")
customGraph.addEdge("B","D")
customGraph.addEdge("D","F")


customGraph.topologicalSort()











# class Topology:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict={}
#         self.gdict=gdict

#     def topologicalSort(self,vertex):
#         li=[vertex]
#         stack=[vertex]
#         while stack:
#             popStack=stack.pop()
#             if popStack not in li:
#                 li.append(popstack)






# gdict ={"A":[],
#         "B":[],
#         "C":["A","B"],
#         "E":["C"],
#         "H":["E"],
#         "F":["E","D"],
#         "G":["F"],
#         "D":["B"]
#     }

# TopologicalSort=Topology(gdict)
# TopologicalSort.topologicalSort("H")

# Instructor Way 






