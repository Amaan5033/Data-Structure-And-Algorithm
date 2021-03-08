
# Floyd Warshell algorithm will run for all vertices
# at one time so it will never detect negative cycle



INF=9999

def printsolution(nv,distance):#nv=number of vertices
    for i in range(nv):
        for j in range(nv):
            if distance[i][j]==INF:
                print("INF",end=" ")
            else:
                print(distance[i][j],end=" ")
        print(" ") 


def FloydWarshell(nv,G):
    distance=G
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

    printsolution(nv,distance) 
#O(v^3),O(V^2)

G=[[0,8,INF,1],
    [INF,0,1,INF],
    [4,INF,0,INF],
    [INF,2,9,0]
]

FloydWarshell(4,G)

















