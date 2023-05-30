# Graph implementation

class Node:

    def __init__(self, val):
        self.vertex = val
        self.next = None


class Graph:

    def __init__(self, vertices):
        
        self.V = vertices
        self.graph = [None]*self.V
        self.adj = [[0 for i in range(self.V)] for j in range(self.V)]

    def create_adj_mat(self, src, dest):

        for i in range(len(self.adj)):
            self.adj[src][dest] = 1
            self.adj[dest][src] = 1

    def create_adj_list(self, src, dest):

        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def add_vertex(self, vertex, dlst):

        self.V += 1
        for i in range(self.V-1):
            self.adj[i].append(0)

        lst = [0 for i in range(self.V)]
        self.adj.append(lst)

        
        self.create_adj_mat(vertex, dlst)
        self.graph.append(None)
        self.create_adj_list(vertex, dlst)
    
    def bfs_for_list(self):

        visited = [False]*self.V
        bfs_traversal = []
        for i in range(self.V):
            if visited[i] == False:
                queue = []
                queue.append(i)
                visited[i] = True
            while queue:

                node = queue.pop(0)
                bfs_traversal.append(node)
                p = self.graph[node]
                while p:
                    if visited[p.vertex] == False:
                        visited[p.vertex] = True
                        queue.append(p.vertex)
                    p = p.next
        return bfs_traversal
    
    def bfs_for_mat(self):
        visited = [False]*self.V
        bfs_traversal = []

        for i in range(self.V):

            if visited[i] == False:
                queue = []
                visited[i] = True
                queue.append(i)
            while queue:

                node = queue.pop(0)
                bfs_traversal.append(node)

                for i, n in enumerate(self.adj[node]):
                    if n == 1 and visited[i] == False:
                        visited[i] = True
                        queue.append(i)
        return bfs_traversal
    def print_adj_list(self):

        for i in range(self.V):
            print(f"List of {i}\nhead", end="")
            temp = self.graph[i]
            while temp:
                print(f"-->{temp.vertex}", end="")
                temp = temp.next
            print()


graph = Graph(4)

graph.create_adj_list(0, 1)
graph.create_adj_list(1, 2)
graph.create_adj_list(1, 3)
graph.create_adj_list(2, 3)


graph.create_adj_mat(0, 1)
graph.create_adj_mat(1, 2)
graph.create_adj_mat(1, 3)
graph.create_adj_mat(2, 3)

graph.add_vertex(4,3)
print(graph.adj)
graph.print_adj_list()

print(graph.bfs_for_list())
print(graph.bfs_for_mat())