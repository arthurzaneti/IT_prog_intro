
# _____________________1_______________________
import numpy as np
import math as m

global TOL 
TOL = 1e-9
# Escolhi uma tolerância de 1e-9 pelo que vi no link abaixo 
#https://www.geeksforgeeks.org/comparing-floating-points-number-for-almost-equality-in-python/?ref=next_article

class Field:
    pass

class VectorSpace:
    """VectorSpace:
    Abstract Class of vector space used to model basic linear structures
    """
    
    def __init__(self, dim: int, field: 'Field'):
        """
        Initialize a VectorSpace instance.

        Args:
            dim (int): Dimension of the vector space.
            field (Field): The field over which the vector space is defined.
        """
        self.dim = dim
        self._field = field
        
    def getField(self):
        """
        Get the field associated with this vector space.

        Returns:
            Field: The field associated with the vector space.
        """
        return self._field
    
    def getVectorSpace(self):
        """
        Get a string representation of the vector space.

        Returns:
            str: A string representing the vector space.
        """
        return f'dim = {self.dim!r}, field = {self._field!r}'
        # return self.__repr__()

    def __repr__(self):
        """
        Get a string representation of the VectorSpace instance.

        Returns:
            str: A string representing the VectorSpace instance.
        """
        # return f'dim = {self.dim!r}, field = {self._field!r}'
        return self.getVectorSpace()
    
    def __mul__(self, f):
        """
        Multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError
    
    def __rmul__(self, f):
        """
        Right multiplication operation on the vector space (not implemented).

        Args:
            f: The factor for multiplication.

        Returns:
            The result of multiplication.

        Note:
            This method is defined in terms of __mul__.
        """
        return self.__mul__(f)
    
    def __add__(self, v):
        """
        Addition operation on the vector space (not implemented).

        Args:
            v: The vector to be added.

        Raises:
            NotImplementedError: This method is meant to be overridden by subclasses.
        """
        raise NotImplementedError

class RealVector(VectorSpace):
    _field = float
    def __init__(self, dim, coord):
        super().__init__(dim, self._field)
        self.coord = coord
    

    @staticmethod
    def _builder(coord):
        raise NotImplementedError


    def __add__(self, other_vector):
        n_vector = []
        for c1, c2 in zip(self.coord, other_vector.coord):
            n_vector.append(c1+c2)
        return self._builder(n_vector)


    def __mul__(self, alpha):
        n_vector = []
        for c in self.coord:
            n_vector.append(alpha*c)
        return self._builder(n_vector)
    
    
    def iner_prod(self, other_vector):
        res = 0
        for c1, c2 in zip(self.coord, other_vector.coord):
            res += c1*c2
        return res


    def __str__(self):
        ls = ['[']
        for c in self.coord[:-1]:
            ls += [f'{c:2.2f}, ']
        ls += f'{self.coord[-1]:2.2f}]'
        s =  ''.join(ls)
        return s
    
    def __sub__(self, v2):
        n_vector = []
        for c1, c2 in zip(self.coord, v2.coord):
            n_vector.append(c1 - c2)
        return self._builder(n_vector)
    
    def __rmul__(self, a):
        return(self * a)
    
    def __eq__(self, v2):
        return((self.coord == v2.coord))

    def __neg__(self):
        return self * -1  


class Vector_3D(RealVector):
    @staticmethod
    def _builder(coord):
        return(Vector_3D(coord))
    
    def __init__(self, coord):
        if len(coord) != 3:
            raise ValueError
        else:
            self.coord = coord

    def __abs__(self):
        s = 0
        for coord in self.coord:
            s += coord**2
        return(np.sqrt(s))
    
    def __eq__(self, v2):
        for i in range(len(self.coord)):
            if abs(self.coord[i] - v2.coord[i]) > TOL:
                return False
        return True
    
    def __gt__(self, v2):
        return (abs(self) - abs(v2) > TOL)

    def __ge__(self, v2):
        return(self > v2 or self == v2)
    
    def __lt__(self, v2):
        return(v2 > self)
    
    def __le__(self, v2):
        return(v2 >= self)
    
"""Testes das funções (parcialmente feito pelo chat, parcialmente por mim)
# Define some 3D vectors
v1 = Vector_3D([1, 2, 3])
v2 = Vector_3D([1, 2.0000001, 3])
v3 = Vector_3D([1, 2, 3.0000000000000000001]) 
v4 = Vector_3D([5, 5, 5])

# Test __eq__
print(f"v1 == v3: {v1 == v3}")  # Expected: True
print(f"v1 == v2: {v1 == v2}")  # Expected: False

# Test __gt__
print(f"v2 > v1: {v2 > v1}")    # Expected: True
print(f"v1 > v4: {v1 > v4}")    # Expected: False
print(f"v4 > v1: {v4 > v1}")    # Expected: True

# Test __ge__
print(f"v2 >= v1: {v2 >= v1}")  # Expected: True
print(f"v1 >= v3: {v1 >= v3}")  # Expected: True
print(f"v4 >= v1: {v4 >= v1}")  # Expected: True

# Test __lt__
print(f"v1 < v2: {v1 < v2}")    # Expected: True
print(f"v4 < v1: {v4 < v1}")    # Expected: False
print(f"v1 < v4: {v1 < v4}")    # Expected: True

# Test __le__
print(f"v1 <= v2: {v1 <= v2}")  # Expected: True
print(f"v1 <= v3: {v1 <= v3}")  # Expected: True
print(f"v1 <= v4: {v1 <= v4}")  # Expected: True
"""

#______________________________2__________________________________
"""
- 1 bit para o sinal 
- ceil(log_2(\beta)) para cada dígito, logo p * ceil(log_2(\beta)) para os digitos d_0, ..., d_{p-1}
- log_2(e_max - e_min + 1) para representar um número entre (inclusive) 0 e e_max - e_min, dai o expoente seria
este número mais e_min 

Logo o total é 1 + p * ceil(log_2(\beta)) + log_2(e_max - e_min + 1)
"""
#____________________________3 e 4________________________________

def calcula_epsilon(ponto, passos = 100):
    DIF = 0.1
    for i in range(passos):
        if ponto + DIF == ponto:
            DIF *= 3/2
        else:
            DIF *= 1/2
    
    return(DIF)
    #Tem a função np.spacing do numpy que faz exatamente isso também

"""
Quanto maior a magnitude do número maior a tolerância na comparação. Isso faz bastante sentido
visto que em geral diferenças em torno do epsilon de máquina são irrelevantes para medidas de magnitude 10**6
Porém, em casos específicos (como astrofísica por exemplo) onde se necessita precisão mesmo para grandes números 
isso pode vir a ser um problema. 

print(calcula_epsilon(1))
print(calcula_epsilon(10**6))
print(calcula_epsilon(10**15))
print(calcula_epsilon(0))
print(calcula_epsilon(-1))
print(calcula_epsilon(-10**6))

Algumas soluções que eu achei para esse problema são:
- Usar math.isclose (ou np.isclose) para comparações com precisão arbitrária
- Usar o modulo Decimal para precisão arbitrária que é a solução mais simples
"""
#_______________________5_______________________

""" O módulo decimal foi feito com aplicações deste tipo em mente, portanto eu o usaria"""
import decimal as d

"""Pequeno snippet que mostra o poder do módulo. Mudando a precisão podemos fazer um código sensível a
difenças de 10**-40 em número de magnitude de 10**40."""
d.getcontext().prec = 81
x = d.Decimal(10**40)
eps = d.Decimal(10**-40)

print(x + eps == x)


