n = int(input("Introduzca un numero entero(Positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")