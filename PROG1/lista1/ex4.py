
def relatively_prime(p,q): #Euclid's algorithm 
    # Apenas garantindo r = p <= q para começar o algoritmo
    if (p > q):
        aux = p
        p = q
        q = aux
        r = q
    else: 
        r = p

    #O algoritmo de fato
    while r > 1:
        r = q % p
        q = p
        p = r
        
    if(r == 0):
        return False
    if(r == 1):
        return True
    else:
        print("Problema na execução do algoritmo")

"""
print(relatively_prime(10**10,9**10))
print(relatively_prime(100,40))
"""