
# Prims Algorithm is a greedy algorithm

# It finds minimum spanning tree for weighted undirected
# graphs 


# Take any vertex as a source set its weight to 0 and 
# all other vertices weight to infinity

# For every adjacent vertices if the current weight is 
# more than current edge then we set it to current edge

# Then we mark current vertex as visited

# Repeat these steps for all vertices in increasing 
# order of weight

from collections import defaultdict

class Prims:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph={}
        self.adjacent=defaultdict(list)
        self.MST=[]


    def add_edge(self,fromNode,toNode,Weight):
        self.graph[(fromNode,toNode)]=Weight
        self.adjacent[fromNode].append(toNode)

    

    def print_solution(self):
        for s,d,w in self.MST:
            print("%s--%s: %s"% (s,d,w))

# My way 
    def primsAlgorithm1(self,src):
        visited=[]
        for i in range(len(self.vertices)-1):
            cost=float("inf")
            for j in self.adjacent[self.vertices[i]]:
                if self.vertices[i] and j not in visited:
                    if self.graph[(self.vertices[i],j)]<cost:
                        cost=self.graph[(self.vertices[i],j)]
                        a,b=self.vertices[i],j
            self.MST.append((a,b,cost))        
            visited.append(self.vertices[i])
        self.print_solution()




# O(V^3),O(V)


# instructor way

    def primsAlgorithm(self):
        visited=[0]*self.vertexNum
        edgeNum=0
        visited[0]=True
        while edgeNum<self.vertexNum-1:
            min=sys.maxsize
            for i in range (self.vertexNum):
                if visited[i]:
                    for j in range(self.vertexNum):
                        if((not visited[j]) and self.edges[i][j]):
                            if min>self.edges[i][j]:
                                min=self.edges[i][j]
                                s=i
                                d=j
            self.MST.append([self.nodes[s],self.nodes[d],self.edges[s][d]])
            visited[d]=True
            edgeNum+=1

            

vertices=["A","B","C","D","E"]

pr=Prims(vertices)


pr.add_edge("A","B",10)
pr.add_edge("B","A",10)
pr.add_edge("A","C",20)
pr.add_edge("C","A",20)
pr.add_edge("B","D",5)
pr.add_edge("D","B",5)
pr.add_edge("B","C",30)
pr.add_edge("C","B",30)
pr.add_edge("C","D",15)
pr.add_edge("D","C",15)
pr.add_edge("D","E",8)
pr.add_edge("E","D",8)
pr.add_edge("C","E",6)
pr.add_edge("E","C",6)



pr.primsAlgorithm1("A")





        


















