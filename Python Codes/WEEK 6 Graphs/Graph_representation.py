#Graph representation

def make_adj_matrix(n,m):
    
    adj = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        u,v = map(int,input().split())
        adj[u][v] = 1
        adj[v][u] = 1
    print(adj)

class AdjNode:
    def __init__(self,data):
        self.vertex = data
        self.next = None

class Graph:

    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None]*self.V

    def add_edge(self,src,dest):            #This is just basic Linked list insertion at the head
        
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node=  AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_adj_list(self):
        for i in range(self.V):
            print(f"Adjacency list of {i}:\nhead",end = "")
            temp = self.graph[i]

            while temp:
                print(f"->{temp.vertex}",end="")
                temp = temp.next
            print("\n")

graph = Graph(4)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(2,3)

graph.print_adj_list()