# python 3.10
import numpy as np
from VectorSpace import VectorSpace

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


class Vector2D(RealVector):
    _dim = 2
    def __init__(self, coord):
        if len(coord) != 2:
            raise ValueError
        super().__init__(self._dim, coord)


    @staticmethod
    def _builder(coord):
        return Vector2D(coord)
    

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
        return((self.coord == v2.coord).all())

    def __neg__(self):
        coords = (self * -1).coord
        return(Vector2D(coords))   
    
    def __str__(self):
        return(str(self.coord))
    
    def __abs__(self):
        s = 0
        for coord in self.coord:
            s += coord**2
        return(np.sqrt(s))

if __name__ == '__main__':
    V2 = Vector2D([1, 2])
    print('V2 = ', V2)
    W2 = Vector2D([3, 4])
    print('W2 = ', W2)


    print(V2.getVectorSpace())

    r = V2+4*W2
    print('V2 + 4*W2 =', r)
    print('(V2 + 4*W2).CW() = ', r.CW())
    print('W2.CCW() = ', W2.CCW())
    print('V2.iner_prod(W2) = ', V2.iner_prod(W2))
    print("V2 - W2 = ", V2 - W2)
    print("abs(V2) =", abs(V2))
    print("-V2 = ", -V2)
