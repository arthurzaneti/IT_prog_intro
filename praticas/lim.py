def lateral_lim(f, a, left, steps, verbose=False):
  eps = 1
  if left:
    eps *= -1
  for i in range(steps):
    if verbose:
      print(f"step:{i}, result = {f(a + eps)}")
    eps /= 10
  return f(a + eps)


def checka_eps(f, a, eps):
  delta = 0.1
  while delta > 10**(-30):
    if abs((f(a + delta) - f(a - delta))) < eps:
      return True
    delta /= 2
  return False


def tem_lim(f, a):
  for i in range(20):
    satisfaz_eps = checka_eps(f, a, 10**(-i))
    if not satisfaz_eps:
      return False
    return True
