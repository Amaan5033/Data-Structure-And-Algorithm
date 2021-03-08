# import QueueList as queue
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

# breadth first Traversal

    # def bfs(self,start,end):
    #     li=[]
    #     customQueue=queue.Queue()
    #     customQueue.Enqueue(start)
    #     while not customQueue.isEmpty():
    #         p=customQueue.Dequeue()
    #         if p not in li:
    #             li.append(p)
    #             for i in range(len(self.gdict[p])):
    #                 customQueue.Enqueue(self.gdict[p][i])
    #     return li

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

# O(E) Because we are visiting only connected vertices 
# Not isolated vertices so number of edges will be 
#greater than vertices so O(E) time complexity

# ,O(E) Number of Edges greater than vertices 

customDict={"a":["b","c"],
            "b":["d","g"],
            "c":["e","d"],
            "d":["f"],
            "e":["f"],
            "g":["f"],

                }

graph=Graph(customDict)
print(graph.bfs("a","g"))