import numpy as np
class Vector:
    def __init__(self, coord):
        self.coord = coord
    
    def __add__(self, v2):
        try:
            vector_sum = Vector(self.coord + v2.coord)
            return vector_sum
        except ValueError:
            return None
    
    def __sub__(self, v2):
        try:
            return Vector(self.coord - v2.coord)
        except ValueError:
            return None

    def __mul__(self, a):
        if type(self) == type(a):
            return(sum(self.coord * a.coord)) 
        else:
            return(Vector(self.coord * a))
    
    def __rmul__(self, a):
        return(self * a)
    
    def __eq__(self, v2):
        return((self.coord == v2.coord).all())

    def __neg__(self):
        return(Vector(self.coord * -1))   
    
    def __str__(self):
        return(str(self.coord))
    
    def __abs__(self):
        s = 0
        for coord in self.coord:
            s += coord**2
        return(np.sqrt(s))

