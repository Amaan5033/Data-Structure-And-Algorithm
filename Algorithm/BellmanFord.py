


# Why does Bellman Ford Run in (Number of Vertices-1) times?

#If any node is acheived better distance in previous 
#Iteration, than that better distance is used to improve
#distance of other vertices


class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]

    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])

    def addNode(self,value):
        self.nodes.append(value)


    def print_solution(self,dist):
        print("Vertex Distance from Source")
        for key,value in dist.items():
            print(" "+key,": ",value)


    def BellmanFord(self,src):
        dist={i: float("inf") for i in self.nodes}
        dist[src]=0

        for _ in range(self.V-1):
            for s,d,w in self.graph:
                if dist[s] != float("inf") and dist[s]+w<dist[d]:
                    dist[d]=dist[s]+w

        for s,d,w in self.graph:
            if dist[s] != float("inf") and dist[s]+w <dist[d]:
                print("Graph contains Negative cycle") 
                return 

        self.print_solution(dist)


#O(EV),O(V)


g=Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")

g.add_edge("A","C",6)
g.add_edge("A","D",6)
g.add_edge("B","A",3)
g.add_edge("C","D",1)
g.add_edge("D","C",2)
g.add_edge("D","B",1)
g.add_edge("E","B",4)
g.add_edge("E","D",2)

g.BellmanFord("E")















