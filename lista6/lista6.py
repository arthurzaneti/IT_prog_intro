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
    if G.node_values[starting_node] == value:
        return starting_node
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
    search = _bfs_search(G, starting_node, value)
    if type(search) == str: #Achei o nó
        return(search)

    while len(search) < len(G.adjacencias.keys()):
        for node in G.adjacencias.keys():
            if node not in search:
                new_start = node
        new_search = _bfs_search(G, new_start, value)
        if type(new_search) == str:
            return(new_search)
        else:
            search += new_search
    
    return(search) #Retorna todos os nós caso não ache o no procurado

"""
G = Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
for node in nodes:
    G.add_vertex(node, node)
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
print(bfs_search(G, "J", "Q"))  # Should not find 'M', return all nodes
"""
#______________________________________3____________________________________________

def count_islands(map):
    visited_pos = []
    island_count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1 and (i,j) not in visited_pos:
                visited_pos += _maximal_component(map, (i, j))
                island_count +=1
    return(island_count)

def _maximal_component(map, pos):
    component = []
    f = Fila()
    f.append((pos))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]
    while not f.is_empty():
        x, y = f.pop()
        component.append((x, y))
        for dx, dy in directions:
            if (x + dx, y + dy) not in component: 
                if 0 <= x + dx and x + dx < len(map) and 0 <= y + dy and y + dy < len(map[0]):
                    if map[x + dx][y + dy] == 1:
                        f.append((x + dx, y + dy))
        
    return(component)

"""
map_example = [
    [0, 0, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

print(count_islands(map_example))
"""
#______________________________________4____________________________________________
import numpy as np
def centroids(map):
    visited_pos = []
    components = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1 and (i,j) not in visited_pos:
                component = _maximal_component(map, (i, j))
                components.append(component)
                visited_pos += component

    smallest, biggest = float("inf"), 0
    for i in range(len(components)):
        if len(components[i]) < smallest:
            smallest = len(component)
            i_smallest = i
        
        if len(components[i]) > biggest:
            biggest = len(component)
            i_biggest = i
    
    centroid_smallest, centroid_biggest = [0,0], [0,0]
    for pos in components[i_smallest]:
        centroid_smallest[0] += pos[0]
        centroid_smallest[1] += pos[1]
    for pos in components[i_biggest]:
        centroid_biggest[0] += pos[0]
        centroid_biggest[1] += pos[1]


    return((centroid_biggest[0] / len(components[i_biggest]),
            (centroid_biggest[1] / len(components[i_biggest]))), 
            (centroid_smallest[0] / len(components[i_smallest]),
             centroid_smallest[1] / len(components[i_smallest])))
"""
map_example = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Call the centroids function
centroid_biggest, centroid_smallest = centroids(map_example)
print("Centroid of the biggest island:", centroid_biggest)
print("Centroid of the smallest island:", centroid_smallest)
"""
#______________________________________5____________________________________________

#Interpretei "4 direções" como não incluindo as diagonais

def lake(map):
    visited_pos = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) not in visited_pos and map[i][j] == 1:
                water_component, is_lake = _maximal_water_component(map, (i, j))
                if is_lake == True:
                    return(True)
                visited_pos += water_component
    
    return(False)


def _maximal_water_component(map, pos):
    component = []
    is_lake = True
    f = Fila()
    f.append((pos))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while not f.is_empty():
        x, y = f.pop()
        component.append((x, y))
        for dx, dy in directions:
            if (x + dx, y + dy) not in component: 
                if 0 > x + dx or x + dx == len(map) or 0 > y + dy or y + dy == len(map[0]):
                    is_lake = False
                else:
                    if map[x + dx][y + dy] == 1:
                        f.append((x + dx, y + dy))
    return(component, is_lake)

"""
no_lake = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

with_lake = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

with_lake_2 = [# conectado diagonalmente com o oceano
    [0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

print(lake(no_lake), lake(with_lake), lake(with_lake_2))
"""
