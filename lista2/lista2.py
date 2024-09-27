import numpy as np

#________________________1__________________________
class MyArray:
    #Decidi arbitrariamente tomar o vetor como sendo de floats sempre
    def __init__(self, size, values = []):
        self.size = size
        self.used_size = len(values)
        if self.used_size > self.size:
            raise ValueError

        array = np.zeros(size)
        for i in range(len(values)):
            array[i] = values[i]

        self.array = array
    
    def append(self, values): #Função feita para o append aceitar lista
        if type(values) in {float, int}:
            self._append1(values)
        else:
            for value in values:
                self._append1(value)
        
    def _append1(self, value):
        if (self.used_size == self.size):
            self._realoc()
        self.array[self.used_size] = value
        self.used_size += 1

    def _realoc(self, up = True):
        if up:
            array = np.zeros(self.size * 2) # Escolhi constante 2 arbitraria para a realocação
        else:
            array = np.zeros(int(np.ceil(self.size/2)))

        for i in range(self.used_size):
            array[i] = self.array[i]
            
        self.array = array
        self.size = len(self.array)

    
    def remove(self, index):
        for i in range(index, self.used_size):
            self.array[i - 1] = self.array[i]
        self.array[self.used_size - 1] = 0 

        self.used_size -= 1
        if self.used_size < self.size / 3: 
            # menor que 1/3 para termos um certo buffer, se eu colocasse 1/2 por exemplo, seria comum uma inserção
            #seguida de uma remoção fazer com que tanto a inserção quanto a remoção sejam O(n).
            self._realoc(up = False)

    def __str__(self):
        rep = "["
        for i in range(self.used_size):
            print(i)
            rep += f"{str(self.array[i - 1])}, "
        rep = rep[0:-2] + "]"
        return(rep)
    
    def __getitem__(self, index):
        if index >= self.used_size:
            raise ValueError
        else:
            return(self.array[index])

# Pelo que pesquisei o python realoca o array com os ponteiros da lista de um modo mais complicado que apenas dobrar
# Ele tem uma função _realoc que é chamada em situações similar a minha (pelo menos no _realoc(up = True)) mas 
#o tamanho do array se torna ceil(1.125 * self.size + 3) para self.size de 1 a 9 e ceil(1.125 * self.size + 6) para 
#self.size > 9.

# Aqui é um teste da inserção e remoção comparando com o a lista do Python. Acabou que minha remoção ficou horrível.
"""
import timeit

m = MyArray(1)
l = list([1])
time_m = timeit.default_timer()
for i in range(100000):
    m.append(1)
print(f"Tempo de inserção MyArray: {timeit.default_timer() - time_m}")

time_l = timeit.default_timer()
for i in range(100000):
    l.append(1)
print(f"Tempo de inserção lista do Python: {timeit.default_timer() - time_l}")

time_m = timeit.default_timer()
for i in range(500):
    m.remove(0)
print(f"Tempo de remoção MyArray: {timeit.default_timer() - time_m}")

time_l = timeit.default_timer()
for i in range(500):
    l.pop(0)
print(f"Tempo de remoção MyArray: {timeit.default_timer() - time_l}")

"""
#________________________2__________________________
class Torus(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return(obj)
    
    def __getitem__(self, index):
        # Tudo de interessante do toro é esse método __getitem__
        return(super().__getitem__(index % len(self)))



