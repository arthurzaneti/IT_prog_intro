from math import exp, sin

import lim
import strdistance

"""
def f1(x):
  if (x < 0):
    return (1 / x**2)
  if (x >= 0):
    return (x)

def f2(x):
  return (sin(x)**7) / exp(x)

print(lim.tem_lim(f1, 0))
"""

print(strdistance.levenshtein_distance("aaaaa", "word2"))
print(strdistance.levenshtein_distance("arthur", "artur"))
print(strdistance.levenshtein_distance("Arthur", "arthur"))
print(strdistance.levenshtein_distance("Gabriel", "arthur"))
print(strdistance.levenshtein_distance("seilaqualquercoisa", "slaqualquercoisa"))