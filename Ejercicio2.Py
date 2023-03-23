n = int(input("Introduce un numero positivo: "))
for i in range(n, -1, -1):
        print(i, end=", ")
while n<0:
    print("No se permiten numeros negativos")
    n = int(input("Introduce un numero positivo: "))
    for i in range(n, -1, -1):
        print(i, end=", ")
        