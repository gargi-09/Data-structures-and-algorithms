# Implementation of Dijkrata's Algorithm

class graph:
    def __init__(self,v):
        self.v = v
        self.graph = [[0 for _ in range(self.v)] for i in range(self.v)]
    
    def printsol(self,dist):
        for node in range(self.v):
            print(node,dist[node])
    
    def min_node(self,dist,vis):
        min = float("inf")
        min_ind = 0
        for u in range(self.v):
            if dist[u]<min and vis[u]==False:
                min = dist[u]
                min_ind = u
        return min_ind
    
    def dijkstra_algo(self,src):
        
        dist = [float("inf")]*self.v
        dist[src] = 0
        vis = [False]*self.v

        for node in range(self.v):
            u = self.min_node(dist,vis)
            vis[u] = True

            for v in range(self.v):
                print(dist)
                if self.graph[u][v]>0 and vis[v]==False and dist[u]+self.graph[u][v]<dist[v]:
                    dist[v] = dist[u]+self.graph[u][v]
        return dist
g = graph(6)
g.graph = [[0,2,4,0,0,0],
           [0,0,1,7,0,0],
           [0,0,0,0,3,0],
           [0,0,0,0,0,1],
           [0,0,0,2,0,5],
           [0,0,0,0,0,0]]
 
dist = g.dijkstra_algo(0)
g.printsol(dist)
 