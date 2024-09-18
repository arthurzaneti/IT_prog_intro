"""1: 
a)
    1
    2

b)
    Value is bad

c)
    que massa!

d)
    [1, 2, 5, 4]
"""

"""2
a) O problema é que o método de inicialização do vetor esta com 
nome errado, deveria ser __init__. Se mudarmos __ints__ para __init__
o código funcionará.

b)
    []
    [2.0, 1.0]

c) É estranho a função "add" retornar o dobro de um dos vetores...
Era esperado que ela somasse os vetores, portanto deveríamos mudar
a linha 20 para "new_vector[i] = self.values[i] + other_vector.values[i]

Também acho retornar uma lista vazia quando os vetores tem tamanhos diferentes
errado, mas isso é questão de preferência. Possivelmente dar erro seria melhor.

"""

#3
import numpy as np

def d_points(p1: tuple, p2: tuple):
    # Função auxiliar útil em ambas classes
    return(np.sqrt((p1[0] - p2[0])**2 + 
                    (p1[1] - p2[1])**2))
class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def inside(self, point):
        # return:
        # 1 if point is inside the circunference
        # 0 if point is on the circunference
        # -1 otherwise
        d = d_points(self.center, point)

        if(d < self.radius):
            return 1
        if(d == self.radius):
            return 0
        else:
            return -1
    
class Line_Segment():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def inside(self, point):
        # Utilizei uma ideia similar a desigualdade triângular onde
        # so vale a igualdade se os pontos são colineares

        d = d_points(self.p1, point) + d_points(self.p2, point)
        if(d == d_points(self.p1, self.p2)):
            return True
        else:
            return False

        # Este método tende a reportar que pontos perto da reta estão na reta, por exemplo ele considera (1.001, 0) como se estivesse na reta
        # Ligando (0,0) a (10,0) por imprecisão numérica

#4

def Line_inside_Circle(line, circle):
   return(2 == circle.inside(line.p1) + circle.inside(line.p2))

#5

class Vector():
    def __init__(self, coordinates: list):
        self.coordinates = coordinates
    
    def diadic_product(self, vector):
        d_prod = []
        for i in range(len(self.coordinates)):
            row = []
            for j in range(len(vector.coordinates)):
                row.append(self.coordinates[i] * vector.coordinates[j])
            d_prod.append(row)
        return(d_prod)
    

