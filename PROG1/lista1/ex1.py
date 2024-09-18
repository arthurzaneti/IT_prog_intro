x = 1
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
for i in l:
    print(i)

x = 2
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
for i in range(len(l)):
    print(l[i])

x = "OLA"
l = [10, 11, x , 13, "Ola", "casa", "carro", "pé"]
i = 0
while l[i] != "carro":
    print(l[i])
    i+=1
