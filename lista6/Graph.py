class Graph:
    def __init__(self):
        self.adjacencias = {}
        self.node_values = {}

    def add_vertex(self, name, value):
        if name not in self.adjacencias:
            self.adjacencias[name] = []
            self.node_values[name] = value
            return True
        return False 

    def add_edge(self, x, y):
        if x not in self.adjacencias:
            self.add_vertex(x, None)
        if y not in self.adjacencias:
            self.add_vertex(y, None)
        
        if y not in self.adjacencias[x]:
            self.adjacencias[x].append(y)
            self.adjacencias[y].append(x)
            return True
        return False

    def remove_vertex(self, name):
        if name in self.adjacencias:
            del self.adjacencias[name]
            del self.node_values[name]
            for neighbors in self.adjacencias.values():
                if name in neighbors:
                    neighbors.remove(name)
            return True
        return False

    def remove_edge(self, x, y):
        if x in self.adjacencias and y in self.adjacencias[x]:
            self.adjacencias[x].remove(y)
            self.adjacencias[y].remove[x]
            return True
        return False

    def neighbors(self, name):
        return self.adjacencias.get(name, [])

    def adjacent(self, x, y):
        return y in self.adjacencias.get(x, [])

    def __str__(self):
        return '\n'.join(f'{node}: {neighbors}' for node, neighbors in self.adjacencias.items())


if __name__ == '__main__':
    # Initialize graph
    G = Graph()

    # Add vertices and edges
    G.add_vertex("a")
    G.add_vertex("b")
    G.add_vertex("c")
    G.add_edge("a", "b")
    G.add_edge("b", "c")

    # Display graph
    print("Graph adjacency list:")
    print(G)

    # Check neighbors
    print("\nNeighbors of 'a':", G.neighbors("a"))
    print("Neighbors of 'b':", G.neighbors("b"))

    # Check adjacency
    print("\nIs 'a' adjacent to 'b'?", G.adjacent("a", "b"))
    print("Is 'b' adjacent to 'a'?", G.adjacent("b", "a"))


