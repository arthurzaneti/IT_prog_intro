#1__________________________________________________________________________________________________________________
def step_combinations(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        return(step_combinations(n - 1) + step_combinations(n - 2)) 
        #step_combinations(n - 1) -> número de modos de subir a escada começando com um degrau
        #step_combinations(n - 2) -> número de modos de subir a escada começando com dois degrau
    
#print(step_combinations(4))

#2 e 3__________________________________________________________________________________________________________________
#CLASSE
import numpy as np
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
    
    def CW(self):
        return Vector2D([-self.coord[1], self.coord[0]])
    

    def CCW(self):
        return Vector2D([self.coord[1], -self.coord[0]])
    
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
        coords = (self * -1).coord
        return(self._builder(coords))   


class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)

    @staticmethod
    def _builder(coord):
        return Vector2D(coord)

    def __abs__(self):
        s = 0
        for coord in self.coord:
            s += coord**2
        return(np.sqrt(s))

# SUBCLASSES
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
    
class Polynomials(RealVector):
    @staticmethod
    def _builder(coord):
        return(Polynomials(coord))
    
    def __init__(self, coord):
        self.coord = coord

    def eval(self, x):
        s = 0
        for i in range(len(self.coord)):
            s += x**i * self.coord[i]
        return(s)
    
    def __str__(self):
        string = ""
        for i in range(len(self.coord)):
            i_coord = self.coord[i]
            if i_coord != 0:
                if i_coord != 1:
                    if i_coord == -1 and i != 0:
                        string += " - "
                    elif i_coord < 0:
                        string += f" {str(i_coord)}"
                    else:
                        string += "+" + f" {str(i_coord)}"
                if i!= 0:
                    string += f"x**{i} "
        return(string)

# Código que o CHAT GPT fez para testar as classes: 

# Test for Vector2D
def test_Vector2D():
    print("Testing Vector2D:")
    
    # Initialize two 2D vectors
    v1 = Vector2D([1, 2])
    v2 = Vector2D([3, 4])

    # Test addition
    print(f"{v1} + {v2} = {v1 + v2}")

    # Test scalar multiplication
    alpha = 2
    print(f"{alpha} * {v1} = {alpha * v1}")

    # Test inner product
    print(f"Inner product of {v1} and {v2} = {v1.iner_prod(v2)}")

    # Test rotation (clockwise and counterclockwise)
    print(f"{v1} rotated clockwise = {v1.CW()}")
    print(f"{v1} rotated counterclockwise = {v1.CCW()}")

    # Test vector subtraction
    print(f"{v1} - {v2} = {v1 - v2}")

    # Test vector negation
    print(f"Negation of {v1} = {-v1}")

    # Test vector equality
    print(f"{v1} == {v1}: {v1 == v1}")
    print(f"{v1} == {v2}: {v1 == v2}")

    print("-" * 50)

# Test for Vector_3D
def test_Vector3D():
    print("Testing Vector_3D:")
    
    # Initialize two 3D vectors
    v3 = Vector_3D([1, 2, 3])
    v4 = Vector_3D([4, 5, 6])

    # Test addition
    print(f"{v3.coord} + {v4.coord} = {(v3 + v4).coord}")

    # Test scalar multiplication
    alpha = 3
    print(f"{alpha} * {v3.coord} = {(alpha * v3).coord}")

    # Test inner product
    print(f"Inner product of {v3.coord} and {v4.coord} = {v3.iner_prod(v4)}")

    # Test vector subtraction
    print(f"{v3.coord} - {v4.coord} = {(v3 - v4).coord}")

    # Test vector negation
    print(f"Negation of {v3.coord} = {(-v3).coord}")

    print("-" * 50)

# Test for Polynomials
def test_Polynomials():
    print("Testing Polynomials:")
    
    # Initialize polynomial
    p1 = Polynomials([1, -2, 3])  # Represents 1 - 2x + 3x^2
    
    # Test polynomial evaluation
    x = 2
    print(f"p1({x}) = {p1.eval(x)}")

    # Test polynomial string representation
    print(f"Polynomial p1: {p1}")

    # Test polynomial addition
    p2 = Polynomials([0, 1, -1])  # Represents x - x^2
    print(f"p1 + p2 = {(p1 + p2).coord}")

    # Test scalar multiplication on polynomial
    alpha = 2
    print(f"{alpha} * p1 = {(p1 * alpha).coord}")

    print("-" * 50)
"""
# Run the tests
test_Vector2D()
test_Vector3D()
test_Polynomials()
"""
#4_______________________________________________________________________________________________________________
#Imagem
#5_______________________________________________________________________________________________________________

import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(1, 11)] + list('JQKA') 
    #Mudei o range para começar em 1 
    #Não é bem um erro começar em 2 mas acho que o baralho deveria incluir cartas de todos os números a partir do 2, nao do 3
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
myDeck = FrenchDeck()
print(myDeck[1])
random.shuffle(myDeck._cards)
