#__________________________________1______________________________________

"""
def find_nb(data, point):
    Dt = data - point
    d = np.linalg.norm(Dt, axis=1)
    idt = np.argmin(d)
    return d[idt], idt

    
 A função find_nb ache o ponto mais próximo a "point" em "data" considerando proximidade via
a norma Euclideana.

Quanto a complexidade observemos, chamando de n o tamanho do vetor data, que a função faz 
3 operações O(n), elas são:
    - Fazer n subtrações em "Dt = data - point
    - Calcular a norma de um vetor de duas dimensões n vezes
    - Achar o valor mínimo do vetor d usando np.argmin()
    
e portanto a complexidade é O(n)"""

#__________________________________2______________________________________
import random
from stack import Stack

def generate_maze(m, n, room = '.', wall = '%', cheese = "o"):
    # Initialize a (2m + 1) x (2n + 1) matrix with all walls (1)
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    def dfs_iterativo():
        paths = Stack()
        x, y = 0, 0
        maze[2 * x + 1][2 * y + 1] = room

        add_paths_to_stack(x, y, paths)
    
        while(paths.is_empty() == False):
            x, y, dx, dy = paths.pop()
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = maze[2 * nx + 1][2 * ny + 1] = room
                add_paths_to_stack(nx, ny, paths)

    def add_paths_to_stack(x, y, paths):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        random.shuffle(directions)
        for dx, dy in directions:
            paths.append((x, y, dx, dy))
        
    dfs_iterativo()
    count = 0
    while True: 
        i = int(random.uniform(0, m)) * 2 + 1
        j = int(random.uniform(0, n)) * 2 + 1
        count += 1
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze

def print_maze(maze):
    for row in maze:
        print(" ".join(map(str, row)))

"""
m, n = 20, 20  # Grid size
random.seed(10110)
maze = generate_maze(m, n)
print_maze(maze)
"""

#__________________________________3______________________________________
# Aproveitando que fiz a 2 iterativamente e que não foi especificado que eu DEVO usar um algoritmo
#recursivo ou não, resolverei a 3 também usando um algoritmo recursivo. Certamente ele é mais complicado
#porém, possivelmente, mais divertido
def acha_queijo(maze, m, n, room = '.', wall = '%', cheese = "o"):
    paths = Stack()
    x, y = [0, 0]
    
    def _add_paths_to_stack_cheese(x, y, paths, came_from = [None, None]): 
        #Os None no default é pra lidar com quando vamos inserir os caminhos disponiveis a partir do bloco inicial       
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        exists_a_path = False
        for dx, dy in directions:
            if dx != came_from[0] or dy != came_from[1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * x + dx + 1][2 * y + dy + 1] == room:
                    paths.append((nx, ny, (-dx, -dy)))
                    exists_a_path = True
        
        return(exists_a_path)
    
    def _rewind_path(path, paths):
        """Esta é a função que retorna o caminho caso encontremos um fim sem saída"""
        i = 0
        x, y, came_from = paths.pop() # posição que queremos achar é a (x, y) + came_from
        dx, dy = came_from
        _add_paths_to_stack_cheese(x, y, paths, came_from)
        while i < len(path):
            if path[i][0] == x + dx and path[i][1] == y + dy:
                break
            i += 1
        return(x, y, came_from, path[0: i+1]) 
        

    _add_paths_to_stack_cheese(x, y, paths)
    path = [(x, y)] # O caminho tomado até o queijo
    while(maze[2*x + 1][2*y + 1] != cheese):
        nx, ny, came_from = paths.pop()
        path.append((nx, ny))
        came_from = (x - nx, y - ny)
        if not _add_paths_to_stack_cheese(nx, ny, paths, came_from):
            x, y, came_from, path = _rewind_path(path, paths)
        else:
            x, y = nx, ny    
    _print_path(maze, path, cheese)

def _print_path(maze, path, cheese):
    for i in range(len(path)):
        x, y = path[i]
        if i+1 != len(path):
            dx, dy = path[i+1][0] - path[i][0], path[i+1][1] - path[i][1] 
        else:
            dx, dy = 0, 0 
        
        maze[2*x + 1][2 *y + 1] = maze[2*x + dx + 1][2*y + dy + 1] = "*"
    
    pos_cheese_x, pos_cheese_y  = path[-1]
    maze[2* pos_cheese_x + 1][2* pos_cheese_y + 1] = cheese
    print_maze(maze)
"""
Devo dizer que meu código não funciona em alguns casos e não entendi porque. 
Certamente é algum problema com a função de dar rewind. Aqui está um exemplo
de quando não funciona
m, n = 10, 10  # Grid size
random.seed(1)
maze = generate_maze(m, n)
acha_queijo(maze, m, n) 

"""
#__________________________________4______________________________________
class Grafo:
    def __init__(self, nos, adjacencias):
        self.nos = nos
        self.adjacencias = adjacencias

    def adjacent(self, x, y):
        tf = False
        for a in self.adjacencias[x]:
            if a == y:
                tf = True
                break
        return(tf)

    def _get_no_by_name(self, name):
        for no in self.nos:
            if no.name == name:
                return(no)
        raise NameError

    def neighbors(self, x):
        Neighbors = []
        for no in self.adjacencias.keys():
            if x in self.adjacencias[no]:
                Neighbors.append(no)
        return(Neighbors)
    
    def add_vertex(self, x):
        if x in self.nos:
            return(False)
        else:
            self.nos.append(x)
            self.adjacencias[x.name] = []
            return(True) 

    def remove_vertex(self, x):
        x = self._get_no_by_name(x)
        if x not in self.nos:
            return False

        self.nos.remove(x)
        self.adjacencias.pop(x, None)
        for arestas in self.adjacencias.values():
            arestas[:] = [a for a in arestas if a != x]
        return True

    def remove_arestas(self, x, y):
        if y in self.adjacencias[x]:
            self.adjacencias[x].remove(y)
            return True
        return False 
    
    def add_aresta(self, x, y):
        if y not in self.adjacencias[x]:
            self.adjacencias[x].append(y)
            return(True)
        return(False)
    
    def get_vertex_value(self, x):
        no = self._get_no_by_name(x)
        return(no.data)
    
    def set_vertex_value(self, x, v):
        no = self._get_no_by_name(x)
        no.data = v
    

class no:
    def __init__(self,name, data):
        self.name = name
        self.data = data

# Create nodes (nos)
a = no("a", 1)
b = no("b", 2)
c = no("c", 3)

# Create a graph with nodes and adjacency list using names
G = Grafo(
    nos=[a, b, c],
    adjacencias={
        "a": ["b"],  # 'a' points to 'b'
        "b": ["c"],  # 'b' points to 'c'
        "c": []      # 'c' points to no one
    }
)

""" #TESTES FEITOS PELO CHATGPT
# Test adjacent function
print(G.adjacent("a", "b"))  # True
print(G.adjacent("a", "c"))  # False

# Test neighbors function
print(G.neighbors("b"))  # ['a']

# Test add_vertex function
new_node = no("d", 4)
print(G.add_vertex(new_node))  # True
print(G.adjacencias)  # {'a': ['b'], 'b': ['c'], 'c': [], 'd': []}

# Test add_aresta function
print(G.add_aresta("a", "c"))  # True
print(G.adjacencias["a"])  # ['b', 'c']

# Test remove_arestas function
print(G.remove_arestas("a", "b"))  # True
print(G.adjacencias["a"])  # ['c']

# Test get_vertex_value and set_vertex_value functions
print(G.get_vertex_value("a"))  # 1
G.set_vertex_value("a", 10)
print(G.get_vertex_value("a"))  # 10

# Test remove_vertex function
print(G.remove_vertex("c"))  # True
print(G.adjacencias)  # {'a': [], 'b': []}

"""