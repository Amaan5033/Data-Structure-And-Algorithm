# Here we are creating a weighted graph by using collection 
# library in python 




from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes=set() #vertices
        self.edges=defaultdict(list)
        self.distances={}#keep the distances of edges

    def addnode(self,value):
        self.nodes.add(value)


    def addedge(self,fromNode,toNode,distance):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)]=distance



# def dijkstra(graph,initial):#initial is initial node
#     visited={initial:0}
#     path=defaultdict(list)

#     nodes=set(graph.nodes)#Storing nodes bcuz we delete in loops

#     while nodes:
#         minNode=None
#         for node in nodes:
#             if node in visited:
#                 if minNode is None:
#                     minNode=node
#                 elif visited[node]<visited[minNode]:
#                     minNode=node
#         if minNode is None:
#             break

#         nodes.remove(minNode)
#         currentWeight=visited[minNode]

#         for edge in graph.edges[minNode]:
#             weight=currentWeight+graph.distances[(minNode,edge)]
#             if edge not in visited or weight<visited[edge]:
#                 visited[edge]=weight
#                 path[edge].append(minNode)


#     return visited,path

def Dijkstra(graph,initial):
    graph.nodes={i :float("inf") for i in graph.nodes}
    graph.nodes[initial]=0
    li=list(graph.nodes)
    print(graph.nodes)
    for i in range(len(graph.nodes)-1):
        for i in range(len(graph.nodes)):
            for edge in graph.edges[li[i]]:
                if graph.nodes[li[i]]+graph.distances[(li[i],edge)]<graph.nodes[edge]:
                    graph.nodes[edge]=graph.nodes[li[i]]+graph.distances[(li[i],edge)]
    print(graph.nodes)


       


    
# O(V^2) because of nested loops that are looping through vertices
# ,O(E) appending visited and path dictionary with edges




customGraph=Graph()
# customGraph.addnode("A")
# customGraph.addnode("B")
# customGraph.addnode("C")
# customGraph.addnode("D")
# customGraph.addnode("E")
# customGraph.addnode("F")
# customGraph.addnode("G")


# customGraph.addedge("A","B",2)
# customGraph.addedge("A","C",5)
# customGraph.addedge("B","E",3)
# customGraph.addedge("B","D",1)
# customGraph.addedge("B","C",6)
# customGraph.addedge("D","E",4)
# customGraph.addedge("E","G",9)
# customGraph.addedge("F","G",7)
# customGraph.addedge("C","F",8)

customGraph.addnode("A")
customGraph.addnode("B")
customGraph.addnode("C")
customGraph.addnode("D")
customGraph.addnode("E")
customGraph.addnode("F")


customGraph.addedge("A","B",1)
customGraph.addedge("A","F",4)
customGraph.addedge("B","C",7)
customGraph.addedge("B","E",2)
customGraph.addedge("B","F",4)
customGraph.addedge("F","C",5)
customGraph.addedge("F","E",3)
customGraph.addedge("C","D",7)
customGraph.addedge("C","E",4)
customGraph.addedge("E","D",6)






print(Dijkstra(customGraph,"A"))


# What if there are some negative cycles in graph 
# In that case the Djikstra Algorithm will never find
#Shortest path because there are inifinite solutions of them

#For such cases we use Bellman Ford Algorithm

# Terminology for below comparison

# U=Unweighted
# D=Directed
# P=Positive
# N=negative
# W=Weighted
# u=undirected


# 1=Stands for supported
# 0=Stands for Unsupported


# Graph Type        BFS     Dijkstra      Bellman Ford    FloydWarshell

# U-u                 1        1              1                 1
# U-D                 1        1              1                 1
# P-W-u               0        1              1                 1
# P-W-D               0        1              1                 1
# N-W-u               0        1              1                 1
# N-W-D               0        1              1                 1
# N-Cycle             0        0              1                 0   