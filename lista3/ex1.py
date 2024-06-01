x = 21
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
for i in l[1:]:
    print(i)

print("_________________________")

x = True or False #True
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
for i in l[1:-3]:
    print(i)

print("_________________________")

x = not True or False #False
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
for i in l[::-3]:
    print(i)

print("_________________________")

l1 = [1,2,3]
l2 = [[11,22,33,44], l1, ["ola", "tchau"]]
l1.append(4)
for z in l2:
    print(z)


