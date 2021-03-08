# Its a greedy algorithm
# It finds minimum spanning tree for weighted undirected
# graphs in two ways

# --Add increasing cost edges at each step
# --Avoid any cycle at each step

class Kruskal:
    def __init__(self,vertices):
        self.vertices=vertices
        self.parent={}
        for v in vertices:
            self.parent[v]=v
        self.distances={}
        self.rank=dict.fromkeys(vertices,0)
        self.MST =[]

    def edge_distances(self,fromNode,toNode,distance):
        self.distances[(fromNode,toNode)]=distance
        
        
    def printSolution(self):
        for s,d,w in self.MST:
            print("%s--%s: %s"%(s,d,w))
    

    def findset(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.findset(self.parent[item]) 

    def union(self,x,y):
        xroot=self.findset(x)
        yroot=self.findset(y)
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]+=1
        
        
        
    def Kruskal(self):
        cost =0
        self.distances={k: v for k, v in sorted(self.distances.items(), key=lambda item: item[1])}
        # print(self.distances)
        for i,j in self.distances:
            if self.findset(i)!=self.findset(j):
                self.MST.append((i,j,self.distances[(i,j)]))
                self.union(i,j)
                cost=cost+self.distances[(i,j)]
        self.printSolution()

        # return cost



vertices=["A","B","C","D","E"]
kr=Kruskal(vertices)
kr.edge_distances("A","B",5)
kr.edge_distances("A","C",13)
kr.edge_distances("A","E",15)
kr.edge_distances("B","A",5)
kr.edge_distances("B","C",10)
kr.edge_distances("B","D",8)
kr.edge_distances("C","A",13)
kr.edge_distances("C","B",10)
kr.edge_distances("C","E",20)
kr.edge_distances("C","D",6)
kr.edge_distances("D","B",8)
kr.edge_distances("D","C",6)
kr.edge_distances("E","A",15)
kr.edge_distances("E","C",20)


# kr.edge_distances("A","B",5)
# kr.edge_distances("B","A",5)
# kr.edge_distances("A","C",35)
# kr.edge_distances("C","A",35)
# kr.edge_distances("C","D",10)
# kr.edge_distances("D","C",10)
# kr.edge_distances("D","B",15)
# kr.edge_distances("B","D",15)
# kr.edge_distances("B","C",20)
# kr.edge_distances("C","B",20)
# kr.edge_distances("B","E",10)
# kr.edge_distances("E","B",10)
# kr.edge_distances("D","E",25)
# kr.edge_distances("E","D",25)






kr.Kruskal()
