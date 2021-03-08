# A minimum spanning tree is a subset of the edges 
# of connected, weighted and undirected graph which

# -Connect all vertices together
# -No cycle
# -Minimum total edge


# Disjoint Set- It is a data structure that keeps 
# track of set of elements which are partitioned 
# into a number of disjoint and non overlapping 
# sets and each sets have representation which helps
# in identifying that sets.

# Three things perform under disjoint set 
# -Make set 
# -Union
# -FInd set


class Disjointset:
    def __init__(self,vertices):
        self.vertices=vertices
        self.parent={}
        for v in vertices:
            self.parent[v]=v
        self.rank = dict.fromkeys(vertices,0)

    def find(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.find(self.parent[item])


    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
        self.rank[xroot]+=1
        print(self.rank)
vertices=["A","B","C","D","E"]
ds=Disjointset(vertices)
print(ds.find("B"))
ds.union("A","B")
ds.union("A","C")
ds.union("B","C")
print(ds.find("B"))
print(ds.find("C"))
ds.union("D","E")


    












