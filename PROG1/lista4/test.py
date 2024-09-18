import exs

x = 2
myList = [1, 2, 3, 4]
myDict = {
    'chave1': 1,
    'chave2': x,
    3 : 'Value',
    (1,2) : 'Nossa que massa!!!',
    'L' : myList
}
x = 3
myDict['L'][2] = 5

print(myDict['chave1'])
print(myDict['chave2'])

print("_______________________________")

print(myDict[3]+' is bad')

print("_______________________________")

print(myDict[(1,2)][6:16])

print("_______________________________")

print(myList)

print("_______________________________")

c = exs.Circle((0,0), 1)
print(c.inside((1,0)))
print(c.inside((0.22,0.78)))

c = exs.Circle((5,-0.2), 0.93)
print(c.inside((5,0)))
print(c.inside((10,-0.2)))


print("_______________________________")

r1 = exs.Line_Segment((0,0), (10,0))
print(r1.inside((1,0)))
print(r1.inside((2,1)))

print("_______________________________")

print(exs.Line_inside_Circle(r1, exs.Circle((0,0), 11)))
print(exs.Line_inside_Circle(r1, exs.Circle((100,100), 200)))
print(exs.Line_inside_Circle(r1, exs.Circle((100,100), 20)))

print("_______________________________")

v1 = exs.Vector([1,2,3]) 
v2 = exs.Vector([3.141592, 2.71828, 1,618033]) # Números aleatórios =) (ou não)
v3 = exs.Vector([299792458, 6.62607015, 1.380649, 5.670374419, 1.602176634])
print("_______________________________")
print(v1.diadic_product(v1))
print("_______________________________")
print(v1.diadic_product(v3))
print("_______________________________")
print(v2.diadic_product(v3))
