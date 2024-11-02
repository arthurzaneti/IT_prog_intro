#______________________________________1____________________________________________
from Graph import Graph
from fila import Fila
def _bfs(G, starting_node):
    adj = G.adjacencias
    visited_nodes = [starting_node]
    f = Fila()
    for neighbour in adj[starting_node]:
        f.append(neighbour)
    
    while not f.is_empty():
        node = f.pop()
        if node not in visited_nodes:
            visited_nodes.append(node)
        for neighbour in adj[node]:
            if neighbour not in visited_nodes:
                f.append(neighbour)
    
    return(visited_nodes)

def bfs(G, starting_node): 
    #Preciso que essa função apenas coordene a busca e não realmente a faça para lidar com 
    #grafos disconexos. Essêncialmente ela so chama _bfs em cada componente conexo 
    visited_nodes = _bfs(G, starting_node)
    while len(visited_nodes) < len(G.adjacencias.keys()):
        for node in G.adjacencias.keys():
            if node not in visited_nodes:
                new_start = node
        visited_nodes += _bfs(G, new_start)
    
    return(visited_nodes)

"""Exemplo do chatGPT
G = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
for node in nodes:
    G.add_vertex(node, None)
edges = [("A", "B"), ("A", "C"), ("D", "E"), ("F", "G"), ("G", "H"), ("H", "F"), ("I", "J")]
for x, y in edges:
    G.add_edge(x, y)
print(G)
print(bfs(G, "A"))
"""
#______________________________________2____________________________________________
def _bfs_search(G, starting_node, value):
    adj = G.adjacencias
    visited_nodes = [starting_node]
    f = Fila()
    for neighbour in adj[starting_node]:
        f.append(neighbour)
    
    while not f.is_empty():
        node = f.pop()
        if G.node_values[node] == value:
            return(node)
        if node not in visited_nodes:
            visited_nodes.append(node)
        for neighbour in adj[node]:
            if neighbour not in visited_nodes:
                f.append(neighbour)
    
    return(visited_nodes)

def bfs_search(G, starting_node, value): 
    #Preciso que essa função apenas coordene a busca e não realmente a faça para lidar com 
    #grafos disconexos. Essêncialmente ela so chama _bfs em cada componente conexo 
    search = _bfs(G, starting_node)
    if type(search) == str: #Achei o nó
        return(search)

    while len(search) < len(G.adjacencias.keys()):
        for node in G.adjacencias.keys():
            if node not in search:
                new_start = node
        new_search = _bfs(G, new_start)
        if type(new_search) == str:
            return(new_search)
        else:
            search += new_search
    
    return(search) #Retorna todos os nós caso não ache o no procurado

G = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
for node in nodes:
    G.add_vertex(node, None)
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "E"),
    ("F", "G"), ("G", "H"), ("H", "I"), ("I", "F"),
    ("J", "K"), ("K", "L"), ("L", "J"), ("L", "M"),
    ("D", "M")
]
for x, y in edges:
    G.add_edge(x, y)
print(G)
print(bfs_search(G, "A", "E"))  # Should find 'E'
print(bfs_search(G, "F", "I"))  # Should find 'I'
print(bfs_search(G, "J", "M"))  # Should not find 'M', return all nodes

#______________________________________3____________________________________________
#______________________________________4____________________________________________
#______________________________________5____________________________________________
