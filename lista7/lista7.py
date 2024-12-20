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

   
#test_larger_minimum_spanning_tree()

"""
É essêncialmente impossível fazer um algoritmo que crie a minimum spanning tree que não realize 
em nenhum momento qualquer tipo de ordenação de arestas. Independente do algoritmo algum tipo de
ordenação deverá ocorrer e, como um grafo conexo com n vértices deve possuir ao menos n-1 arestas,
o algoritmo é no mínimo omega((n-1)log(n-1)) = omega(nlogn). 

Não acredito que isso seja uma prova, porque eu não provei que realmente precisamos ordenar as 
arestas. Mas acho que é uma explicação plausível.
"""

"""
Quanto ao meu algoritmo, ele é péssimo. No m-ésimo ponto roda um loop onde ocorrem (m-1)(m+1)
comparações então o algoritmo é ao menos n**2 e portanto não é optimo (talvez n**3?)"""

#______________________________________3__________________________________________
import scipy as sp
from root_finder import bissect, Interval, RealFunction

x = [15, 9, 5, 3, -2, -5, -15]
y = [200, 400, 600, 800, 1000, 1200, 1400]

#poly = sp.interpolate.lagrange(x, y)
#print(poly(0))

#f = RealFunction(f = lambda x: poly(x) - 700, domain = Interval(-15, 15))

#root = bissect(f, Interval(15, -15))
#print(root.min, poly(root.min)) #Lado esquerdo do intervalo mas podia ser qualquer ponto nele

"""Devo dizer que não sei se eu podia usar o scipy e o root_finder nesse exercício,
mas enfim, acho que entendi o código do root_finder melhor usando ele aqui então acho
que pelo aprendizado valeu a pena. Especialmente essa ideia de uma classe para Intervalos
e funções reais é nova para mim."""
#______________________________________4__________________________________________
from root_finder import newton_root, grid_search

def g1(x):
    return x**3 - x
def g1_prime(x):
    return 3*x**2 - 1
def g2(x):
    return np.exp(x) - x**2 + 5
def g2_prime(x):
    return np.exp(x) - 2*x 
"""
G1 = RealFunction(g1, g1_prime, Interval(-100, 100))
G2 = RealFunction(g2, g2_prime, domain = Interval(-10, 10))
root1_1_newton = newton_root(G1, Interval(0.5, 1.5)) 
root1_2_newton = newton_root(G1, Interval(-0.5, 0.5)) 
root2_newton = newton_root(G2, Interval(-10, 10))

print(root1_1_newton, root1_2_newton, root2_newton)

#Ja dei um exemplo usando bissect no exercício 3 mas aqui vai outro

search_space = grid_search(G2, grid_freq=20)
root2_bissec = bissect(G2, search_space)
print(root2_bissec)

"""
#______________________________________5__________________________________________

from poly_interpolant import scipy_interpolater, VandermondeMatrix
from time import perf_counter # Descobri essa função útil
import matplotlib.pyplot as plt

times_scipy = []
times_Vandermonde = []
"""
for i in range(int(1e2)):
    x = np.sort(np.random.uniform(i, -i, i))
    y = np.sort(np.random.uniform(i, -i, i))
    start_time = perf_counter()
    scipy_interpolater(x, y)
    end_time = perf_counter()
    times_scipy.append(end_time - start_time)

    start_time = perf_counter()
    VandermondeMatrix(x, y)
    end_time = perf_counter()
    times_Vandermonde.append(end_time - start_time)

indices = list(range(int(1e2)))

plt.plot(indices, times_scipy, label="scipy_interpolater", color="blue", marker="o")
plt.plot(indices, times_Vandermonde, label="VandermondeMatrix", color="red", marker="x")
plt.title("Performance por métodos de interpolação")
plt.legend()
plt.grid(True)
plt.show()
"""

# E o método da matrix de Vandermonde aparentemente é muito melhor...