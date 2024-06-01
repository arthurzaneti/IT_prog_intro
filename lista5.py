import time

#_____________________________________________1________________________________________________
# Para isso irei implementar a lista encadeada e uma pilha

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

"""
l = [1,2,3,4,5]
cl = create_chained_list(l)
cl.print_list()
cli = cl.inverte_ordem()
print("______________________")
cli.print_list()
"""
# Nesse algoritmo eu passo por todos elementos uma vez para criar o stack e outra vez para criar a nova lista. Certamente existem algoritmos
#melhores, mas acredito que esse seja O(n)


#_____________________________________________2________________________________________________

def roman(n):
    algarisms = ((1000,"M"),
         (500,"D"),
         (100,"C"),
         (50,"L"),
         (10, "X"),
         (5,"V"),
         (1, "I"))
    
    l = [0] * 7 #quantidade de algarismos 
    for i in range(7):
        l[i] = n//algarisms[i][0]
        n = n % algarisms[i][0]
    
    roman_n = ""
    for i in range(7):
        if l[i] == 4:
            roman_n += algarisms[i][1] + algarisms[i-1][1]
        else:
            roman_n += l[i] * algarisms[i][1]
    print(roman_n)

"""
roman(14)
roman(135)
roman(3645)
"""

#__________________________________________3__________________________________________________

import math
def potencia_ruim(x, power):
    xp = 1
    for i in range(power):
        xp *=x
    
    return(xp)
    

# Função auxiliar para a potência boa, explico melhor o porque dessa função nos comentários da função.
# O importante é que binary(n) converte um n pra binário em O(log(n))
def binary(n):
    bin = ""
    i = 1
    while(n > 0):
        digit = n % 2 
        n = (n-digit)/2
        bin = str(int(digit)) + bin
        i += 1
    return(bin) 

def potencia(x, power):
    """
        A lógica do algoritmo é que podemos utilizar recursão para calcular x^{2^n} em so n operações. Por exemplo se
      gostariamos de obeter x^8, basta calcular x^2, dai (x^2)^2 = x^4 então obtemos x^4 com 2 operações e x^8 = (x^4)^2
      e então obtemos x^8 com so 3 = log2(8) operações.
        Dessa facilidade para escrever as potências x^{2^n} gostaríamos de escrever qualquer power usando termos dessa
      forma, por isso pego a representação binária da potência usando a função binary. Então por exemplo 10 é 1010 em 
      binario, então x^10 = x^8 * x^2 onde x^2 e x^8 são calculados rapidamente.
        Não posso afirmar com certeza, mas a meu ver esse algoritmo é O(log(n))
    """
    if(power == 0):
        return(1)
    power_negative = power < 0
    log_floor = math.floor(math.log2(abs(power)))
    xps = [x]
    i = 0
    
    while(i < log_floor):
        xps.insert(0, xps[0]*xps[0])
        i += 1
    bin_power = binary(abs(power))

    xp = 1

    for i in range(len(bin_power)):
        if(int(bin_power[i] == "1")):
            xp *= xps[i]
    if(power_negative):
        return(1/xp)
    return(xp)
print(potencia(3, -42))


