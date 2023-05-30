# BFS AND DFS FOR CONNECTED AND DISCONNECTED GRAPHS

class Graph:

    def  __init__(self,v):
        self.v = v
        self.graph = [[] for i in range(self.v+1)]

    def add_node(self,ind,node):

        self.graph[ind].append(node)
    
    def bfs(self):              # Doesn't account for disconnected graphs

        bfs_traversal = []
        visited = [False]*self.v
        queue = []
        queue.append(0)
        visited[0] = True

        while queue:
            node = queue.pop(0)
            bfs_traversal.append(node)

            for i in self.graph[node]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i] = True
        return bfs_traversal
    
    def bfs_disconnected(self):     # Accounts for disconnected graphs
        bfs_traversal = []
        visited = [False]*self.v

        for i in range(self.v):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True

            while queue:
                node = queue.pop(0)
                bfs_traversal.append(node)

                for i in self.graph[node]:
                    if visited[i]==False:
                        queue.append(i)
                        visited[i] = True
        return bfs_traversal
    
    def dfs_util(self,x,visited,dfs_traversal):

        visited[x] = True
        dfs_traversal.append(x)
        for i in self.graph[x]:
            if visited[i]==False:
                self.dfs_util(i,visited,dfs_traversal)
    
    def dfs(self):          # Doesn't account for disconnected graphs
        visited = [False]*self.v
        dfs_traversal=[]

        self.dfs_util(0,visited,dfs_traversal)
        return dfs_traversal
    
    def dfs_disconnected(self):     # Accounts for disconnected graphs
        visited = [False]*self.v
        dfs_traversal = []

        for i in range(self.v):
            if visited[i] == False:
                self.dfs_util(i,visited,dfs_traversal)
        return dfs_traversal

g = Graph(5)
g.add_node(0,1)
g.add_node(0,2)
g.add_node(0,3)
# g.add_node(3,4)
print(g.graph)

print(g.dfs_disconnected())

