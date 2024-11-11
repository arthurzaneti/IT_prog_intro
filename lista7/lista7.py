#______________________________________1__________________________________________

def find_judge(n, trust):
    # trust tem que ter pessoas com índice até no máximo n-1
    trust_sum = n * [0]
    for truster, trusted in trust:
        trust_sum[truster] -= 1
        trust_sum[trusted] += 1

    for i in range(len(trust_sum)):
        if trust_sum[i] == n-1:
            return(i)
    return(-1) 

#______________________________________2__________________________________________
import numpy as np
import vector

def minimum_spanning_tree(points):
    # Assumo points ser uma lista de elementos da classe vector
    visited = [points[0]]
    unvisited = points.copy()
    unvisited.remove(points[0])
    edges = []
    while len(visited) != len(points):
        min_edge = ([], float("inf"))
        for vertex1 in unvisited:
            for vertex2 in visited:
                edge_len = abs(vertex1 - vertex2)
                if edge_len < min_edge[1]:
                    min_edge = ([vertex2, vertex1], edge_len)
        unvisited.remove(min_edge[0][1])
        visited.append(min_edge[0][1])
        edges.append(min_edge[0])
    return(edges)
#Teste do chatgpt:
def test_larger_minimum_spanning_tree():
    # Define points as Vector objects in a known configuration
    points = [
        vector.Vector(np.array([0, 0])),
        vector.Vector(np.array([2, 0])),
        vector.Vector(np.array([1, 1])),
        vector.Vector(np.array([1, -1])),
        vector.Vector(np.array([3, 0]))
    ]
    
    # Expected MST connections based on minimal distances
    expected_edges = [
        (points[0], points[2]),  # (0, 0) to (1, 1)
        (points[0], points[3]),  # (0, 0) to (1, -1)
        (points[1], points[2]),  # (2, 0) to (1, 1)
        (points[1], points[4])   # (2, 0) to (3, 0)
    ]
    
    expected_edges_count = len(points) - 1

    # Calculate MST
    edges = minimum_spanning_tree(points)
    print("Edges:", [(str(edge[0]), str(edge[1])) for edge in edges])  # Print edges for clarity

   
test_larger_minimum_spanning_tree()
#______________________________________3__________________________________________
#______________________________________4__________________________________________
#______________________________________5__________________________________________