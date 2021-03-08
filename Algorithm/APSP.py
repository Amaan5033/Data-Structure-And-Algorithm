


# Definition- All pair shortest path problem is about 
#finding a path between every vertex to all other vertices
#in a graph such that the total distance between them
#(source and destination) is minimum 

# We will run Djikstra Algorithm for All vertices
# We can also run BFS for all vertices 
# We can also run Bellman Ford for all vertices


#Below is the example for Djikstra Algorithm and BFS


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



def dijkstra(graph,initial):#initial is initial node
    visited={initial:0}
    path=defaultdict(list)

    nodes=set(graph.nodes)#Storing nodes bcuz we delete in loops

    while nodes:
        minNode=None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode=node
                elif visited[node]<visited[minNode]:
                    minNode=node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight=visited[minNode]

        for edge in graph.edges[minNode]:
            weight=currentWeight+graph.distances[(minNode,edge)]
            if edge not in visited or weight<visited[edge]:
                visited[edge]=weight
                path[edge].append(minNode)


    return visited,path


customGraph=Graph()
customGraph.addnode("A")
customGraph.addnode("B")
customGraph.addnode("C")
customGraph.addnode("D")
customGraph.addnode("E")
customGraph.addnode("F")
customGraph.addnode("G")


customGraph.addedge("A","B",2)
customGraph.addedge("A","C",5)
customGraph.addedge("B","E",3)
customGraph.addedge("B","D",1)
customGraph.addedge("B","C",6)
customGraph.addedge("D","E",4)
customGraph.addedge("E","G",9)
customGraph.addedge("F","G",7)
customGraph.addedge("C","F",8)


for i in customGraph.nodes:
    print(dijkstra(customGraph,i))

#-----------------Binary First Search--------------#



class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)



    def bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path
            for adjacent in self.gdict.get(node,[]):#.get(keyname,value)
                new_path=list(path)
                new_path.append(adjacent)
                queue.append(new_path)



customDict={"a":["b","c"],
            "b":["d","g"],
            "c":["e","d"],
            "d":["f"],
            "e":["f"],
            "g":["f"],

                }

graph=Graph(customDict)

if __name__=="__main__":
    testcases=list(customDict)
    a=1
    for i in range(len(testcases)):
        b=a
        for j in range(b,len(testcases)):
            print(graph.bfs(testcases[i],testcases[b]))
            b+=1
        a+=1 
