# Graph directed implementation

class Graph:
    
    def __init__(self, num_of_nodes, directed = True):

        self.num_of_nodes = num_of_nodes
        self.directed = directed
        self.list_edges = []

    def add_edge(self, src, dest, weights):

        self.list_edges.append([src,dest,weights])

        if not self.directed:
            self.list_edges.append([dest, src, weights])
    
    def delete_an_edge(self, src, dest, weights):
        pass
    
    def print_edge_list(self):

        for i in self.list_edges:
            print(f"{i[0]}, {i[1]}, {i[2]}")

graph = Graph(4)

graph.add_edge(0, 1, 0)
graph.add_edge(1, 2, 0)
graph.add_edge(1, 3, 0)
graph.add_edge(2, 3, 0)

graph.print_edge_list()