def sum2list(l1,l2):
    r = []
    for n1 in l1:
        c = []
        r.append(c)
        for n2 in l2:
            c.append(n1*n2)
    return r

print(sum2list([1], [3,5,6]))
r = sum2list([1,2], [3,5,6])
print(r[1][2])
