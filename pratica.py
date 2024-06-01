def linear_combination(p, q, scalar1 = 1, scalar2 = 1):
    h = {}
    print(set(p.keys()).union(set(q.keys())))
    for i in set(p.keys()).union(set(q.keys())):
        if i in p:
            c1 = p[i]
        else:
            c1 = 0
        if i in q:
            c2 = q[i]
        else:
            c2 = 0
        h[i] = (c1*scalar1 + c2*scalar2)
    return(h)  

P = {0:2, 43:-24, 200:2}
Q = {0:-1, 43:-36, 200:3, 201:-1}

LC = linear_combination(P, Q)
print(LC)

