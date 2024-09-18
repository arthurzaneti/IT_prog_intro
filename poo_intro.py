import random

class animal:
    def __init__(self, tipo, nome = None):
        self.tipo = tipo
        self.nome = nome
    
    def __str__(self):
        return(f"{self.tipo}: {self.nome}")
    
class cavalo(animal):
    def __init__(self, nome = None):
        self.tipo = "cavalo"
        self.nome = nome
    
    def trotar(self):
        print("pocoto pocoto pocoto")
    
    def dormir(self):
        x = random.randint(0,1)
        if (x == 1):
            print(f"{self.name} esta dormindo em pe")
        else:
            print(f"{self.name} esta dormindo deitado")
    
class cachorro(animal):
    def __init__(self, nome = None):
        self.tipo = "cachorro"
        self.nome = nome

    def latir(self):
        print("auauauauaua")
    
    def morder(self, animal):
        print(f"{self.nome} mordeu {animal.nome}")
    
    def cavalgar(self, cavalo):
        print(f"O cachorro {self.nome} esta cavalgando {cavalo.nome}...")
        print(f"Ele cavalgou por {random.randint(1,100)} segundos")

class chihuahua(cachorro):
    def __init__(self, nome = None):
        self.tipo = "cachorro"
        self.nome = nome
        self.raça = "chihuahua"
    
    def latir(self):
        print("Awoo-wooo-wooo!")

class beagle(cachorro):
    def __init__(self, nome = None):
        self.tipo = "cachorro"
        self.nome = nome
        self.raça = "beagle"
    
    def latir(self):
        print("Yip-yip-yip!")

arnaldo = cavalo("arnaldo")
dogao = cachorro("dogao")
dogao.latir()
dogao.cavalgar(arnaldo)
dogao.morder(arnaldo)
print("_____________________________")

biggy = beagle("biggy")
lutz = chihuahua("lutz")
biggy.latir()
lutz.latir()
print(biggy)