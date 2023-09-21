# Graph Implementation
class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.next = None
class Graph:
    def __init__(self,V):
        self.v = V
        self.graph = [None]*(V+1)
        self.adj = [[0 for i in range(self.v+1)] for j in range(self.v+1)]
    
    def create_adj_mat(self,src,dest):
        for i in range(1,len(self.adj)):
            self.adj[src][dest] = 1
            self.adj[dest][src] = 1
    
    def create_adj_list(self,src,dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
    
    def display_mat(self):
        for i in range(1,self.v+1):
            for j in range(1,self.v+1):
                if self.adj[i][j]==1:
                    print(f"{i}-->{j}")
        print("matrix ends")
    
    def display_list(self):
        for i in range(1,self.v+1):
            node = self.graph[i]
            print(f"{i}-->",end="")
            while node:
                print(f"{node.vertex}-->",end="")
                node = node.next
            print("Null")

# g = Graph(3)
# g.create_adj_mat(1,2)
# g.create_adj_mat(2,3)
# g.create_adj_mat(3,1)
# g.display_mat()

# g.create_adj_list(1,2)
# g.create_adj_list(2,3)
# g.create_adj_list(3,1)
# g.display_list()
