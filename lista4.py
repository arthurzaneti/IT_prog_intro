#___________________________________________________1_________________________________________________________
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
    
    def balanced(self):
        if self.left == None and self.right == None:
            return True
        
        if self.left == None and self.right != None:
            return(self.right.right == None and self.right.left == None)
        
        if self.left != None and self.right == None:
            return(self.left.right == None and self.left.left == None)
        
        if self.left != None and self.right != None:
            return(self.left.balanced() and self.right.balanced())
        
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.right.right.right.right = TreeNode(9)

print(root.balanced())
print(root.left.balanced())
"""
#___________________________________________________2_________________________________________________________
from random import randint
from timeit import default_timer
import matplotlib.pyplot as plt
import numpy as np

class rstack:
    def __init__(self, data):
        self.stack = data
        self.size = len(data)
    
    def push(self, val):
        self.data.append(val)
        self.size += 1
    
    def pop(self, index = "random"): #index deve ser "random" ou "top". 
        #Como no anunciado diz "estender" ainda deixei o pop com a possibilidade de ser usado deterministicamente
        if index == "random":
            index = randint(0, self.size-1)
            top = self.stack[-1]
            self.stack[-1] = self.stack[index]
            self.stack[index] = top
            self.pop(index = "top")
        else:
            self.stack.pop(-1)
            self.size -= 1

"""
stack = rstack(list(range(1000000)))
times = []
while stack.size != 0:
    ti = default_timer()
    stack.pop()
    times.append(default_timer() - ti)

# Média movel pra evitar dados MUITO distoantes:
times_mm = np.convolve(times, np.ones(10)/10, mode='valid')
plt.plot(times_mm)
plt.show()
"""
"""O importante de ver no gráfico é que o tempo de remoção não é uma função do tempo.
Eu achei surpreendente o quanto o tempo de remoção oscila, em geral, mesmo com médias móveis, o
gráfico é cheio de ruído."""

#___________________________________________________3_________________________________________________________


# Para Breath-First Search eu não achei um jeito de fazer sem uma estrutura de dados auxiliar, mas evitei
#a pilha no Depth-First Search
class Fila:
    def __init__(self, data = []):
        self.data = data
    
    def append(self, data):
        self.data.append(data)
    
    def pop(self):
        self.data = self.data[1:len(self.data)]
    
    def peek(self):
        return(self.data[0])
    
class FTree: #f de flexível
    def __init__(self, val):
        self.val = val
        self.sons = []
    
    def add_son(self, fTree):
        self.sons.append(fTree)
    
    def rem_son(self, index):
        self.sons.pop(index)
    
    def depth_search(self, val):
        if self.val == val:
            return True
        for fTree in self.sons:
            if fTree.depth_search(val) == True:
                return True
        return False

    def breadth_search(self, val, fila = None):
        if self.val == val:
            return True
        
        if fila == None:
            fila = Fila(data = [self])
            return(self.breadth_search(val, fila = fila))

        for fTree in self.sons:
            fila.append(fTree)

        fila.pop()        
        if len(fila.data) == 0:
            return(False)
        else:
            return(fila.peek().breadth_search(val, fila))
            
    #def __str__(self):

root = FTree(1)
root.add_son(FTree(2))
root.add_son(FTree(3))
root.add_son(FTree(4))
root.sons[0].add_son(FTree(10))
root.sons[0].add_son(FTree(11))
root.sons[0].add_son(FTree(12))
root.sons[0].add_son(FTree(13))

#print(root.depth_search(13))
#print(root.breadth_search(13))

#___________________________________________________4_________________________________________________________

import scipy as sp

def random_values(N, distrib):
    if distrib == "Uniform":
        rvs = sp.stats.uniform.rvs(size = 2*N, loc = -1, scale = 2)
    if distrib == "Normal":
        rvs = sp.stats.norm.rvs(size = 2*N, loc = 0, scale = 0.5)
    if distrib == "Student t":
        """
        Na lista pede média 0 e variância 0.5 mas a student tem como parâmetro só graus de liberdade \ni
        Segundo o wikipédia a média da Student t é sempre 0 independente \ni, mas a variância é \ni/(\ni - 2)
        para \ni > 2, em particular é sempre maior que 1 > 0.5. Enfim, falei com o professor presêncialmente
        e ele disse para mim não me preocupar então coloquei, arbitrariamente, \ni como 1.
        """
        rvs = sp.stats.t.rvs(size = 2*N, df = 1)
    return np.reshape(rvs, (N,2))

#print(random_values(10, "Student t"))

#___________________________________________________5_________________________________________________________
def ConvexHull(points):
    convexhull = sp.spatial.ConvexHull(points)
    indices = convexhull.vertices
    l = []
    for i in indices:
        l.append(points[i])
    return(l)

points = random_values(10, "Normal")
print(ConvexHull(points))
    

    
    
