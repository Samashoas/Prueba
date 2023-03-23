class producto:
    def __init__(self, codigo, nombre, precio, marca, frase):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.frase = frase

    def codigo(self):
        return self.__codigo

    def nombre(self):
        return self.__nombre
    
    def precio(self):
        return self.__precio
    
    def marca(self):
        return self.__marca
    
    def frase(self):
        return self.__frase

    def calcular_total(self, unidades):
        return self.precio * unidades
    
    def __str__(self):
        return "-Codigo: " + str(self.codigo) + " -nombre: " + str(self.nombre) + " -precio: " + str(self.precio) + " -marca: " + str(self.marca) + ", " + str(self.frase)

p1 = producto(1, "Elden ring", 60, "Fromsoftware", "Oh elden ring")
p2 = producto(2, "Sekiro", 60, "Fromsoftware", "El camino del shinobi")
p3 = producto(3, "Hollow knight", 15, "Team cherry", "sweet round games")

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(12))
print(p2.calcular_total(14))
print(p3.calcular_total(20))
