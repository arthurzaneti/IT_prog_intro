import numpy as np

def relatively_prime(p,q):
    n_to_check = np.arange(2, min(p,q) + 1)
    while(n_to_check.size != 0):
        k = n_to_check[0]
        if(p % k == 0):
            if(q % k == 0):
                return(False)
        n_to_check = n_to_check[n_to_check % k != 0]
    return(True) 

"""
print(relatively_prime(101, 202))
print(relatively_prime(7853, 7817))
print(relatively_prime(2*7853, 8*7817))
"""