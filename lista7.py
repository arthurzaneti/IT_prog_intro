import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#1)
def write_data():
    poly = lambda x: x**8 -3*x**4 + 2*x**3 - 2*x**2 - x + 2
    x = np.linspace(-3/2, 3/2, 1000)
    y = poly(x)

    file = open("poly_graph_data.txt", "w")
    for i in range(len(x)):
        file.write(str((x[i], y[i])) + "\n")

def read_data():
    file = open("poly_graph_data.txt", "r")
    data = file.readlines()
    x = np.zeros(len(data))
    y = x.copy()
    for i in range(len(data)):
        line = data[i][1:-2].split(",")
        x[i] = float(line[0])
        y[i] = float(line[1])
    return(pd.DataFrame({"x" : x, "y" : y}))

#Código abaixo comentado apenas para não rodar toda vez que o rodo o script
"""

write_data()
data = read_data()

fig, ax = plt.subplots()
plt.plot(data["x"], data["y"])
plt.grid()
plt.show()
"""
#__________________________________________________________________________________________________________________

#2)

# Irei assumir intervalos fechados pela notação [] ao invés de ()
def merge_intervals(intervals):
    interval_borders = []
    for i in intervals:
        # 0 indica inicio de intervalo e 1 indica final
        interval_borders += [tuple([i[0], 0]), tuple([i[1], 1])]

    # Infelizmente utilizo uma função lambda para poder ordenar a lista de tuplas pela primeira entrada
    interval_borders.sort(key= lambda x:x[0])
    # Se algum ponto aparecer como fim e início de intervalo, ele é irrelevante e pode ser removido
    # a não ser que seja o primeiro ou último ponto, nesse caso um dos intervalos deve ser mantido
    interval_borders_f = []
    i = 0
    while i < len(interval_borders):
        if i == len(interval_borders) - 1:
                interval_borders_f.append(interval_borders[-1])
        elif interval_borders[i][0] == interval_borders[i+1][0]:
            if i == 0:
                interval_borders_f.append(interval_borders[0])
                i +=1
        else:
            interval_borders_f.append(interval_borders[i])
        i +=1
    
    #O loop que de fato junta os intervalos
    merged_intervals = []
    counter = 0 
    while(len(interval_borders_f) != 0):
        if counter == 0:
            left = interval_borders_f[0][0]
        if interval_borders_f[0][1] == 0:
            counter += 1
        else: #interval_borders[0][0] == 1
            counter -= 1
        popped = interval_borders_f.pop(0)
        if counter == 0:
            merged_intervals.append([left, popped[0]])
    return(merged_intervals)
    
#print(merge_intervals([[1,3], [2,6], [4,9], [2,3], [11,33], [12,13]]))

#_______________________________________________________________________________________
#3)

# Apenas busca binária
def missing_int(ints):
    while(len(ints) > 2):
        pos = int(len(ints)/2)
        if(ints[pos] - ints[0] > pos):
            ints = ints[0:pos+1]
        else:
            ints = ints[pos:len(ints)]
    return(int((ints[0] + ints[1])/2))

#print(missing_int([1,3,4,5,6,7,8,9,10,11,12]))

#_______________________________________________________________________________________
#4) 

#Copiei minha implementação da lista encadeada e da inversão dela da outra lista
class stack:
    def __init__(self, data = []):
        self.data = data
        self.n_elem = len(data)
    
    def add(self, elem):
        self.data.insert(0, elem)
        self.n_elem += 1
    
    def pop(self):
        self.n_elem -= 1
        return(self.data.pop(0))
    
class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def print_list(self):
        n = self
        while(n != None):
            print(n.data)
            n = n.next
    
    def inverte_ordem(self):
        s = stack()
        n = self
        while(n != None):
            s.add(n)
            n = n.next

        head = s.pop()
        n = head
        while(s.n_elem > 0):

            n.next = s.pop()
            n = n.next
        
        n.next = None
        return(head)
    
    # Novo método copy, apenas duplica os nós da lista
    def copy(self):
        n = self
        nc = node(n.data)
        head = nc
        while(n.next != None):
            nc.next = node(n.next.data)
            n = n.next
            nc = nc.next
        return(head)

    def is_palindrome(self):
        n = self
        nc = self.copy().inverte_ordem()
        while (n != None):
            if(n.data != nc.data):
                return(False)
            n = n.next
            nc = nc.next
        return(True)        
#Criar uma lista encadeada a partir de uma lista
def create_chained_list(l):
    head = node(l[0])
    n = head
    i = 1
    while i < len(l):
        n.next = node(l[i])
        n = n.next 
        i += 1

    return(head)

#_____________________________________________________________________

#5)
import numpy as np
class Vector3D:
    def __init__(self, coord):
        self.coord = coord
    
    def proj(self, w):
        return(w * (self * w)/(w * w))
    
    def __add__(self, v2):
        try:
            vector_sum = Vector3D(self.coord + v2.coord)
            return vector_sum
        except ValueError:
            return None

    def __mul__(self, a):
        if type(self) == type(a):
            return(sum(self.coord * a.coord)) 
        else:
            self.coord *= a
            return(self)
    
    def __rmul__(self, a):
        return(self * a)
    
    def __eq__(self, v2):
        return((self.coord == v2.coord).all())

    def __neg__(self):
        return(self.coord * -1)   
    
    def __str__(self):
        c = self.coord
        return(f"[ {c[0]}, {c[1]}, {c[2]}]")


v1 = Vector3D(np.array([1,-1, 0]))
v2 = Vector3D(np.array([1, 1, 0]))
v3 = Vector3D(np.array([0, 0, 1]))

# Exemplo de operações básicas
print(2*v1 + 3*v2 + v3) 


