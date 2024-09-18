from ex3 import average
from ex4 import minus_sum

def sqrt(n):
    guess = n
    while abs(guess**2 - n) > n/10**6:
        guess = (guess + n/guess)/2
    return(guess)
 
def std_deviation(l):
    l = minus_sum(l, average(l))
    for i in range(len(l)):
        l[i] = l[i]**2
    return(sqrt(sum(l)))

"""
print(std_deviation([1,1,1,1,1,1]))
print(std_deviation([1,2,3,4,5,6]))
print(std_deviation([2,4,6,8,10,12]))
"""