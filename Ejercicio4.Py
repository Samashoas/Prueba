nombre = input("Intoduzca su nombre: ")
Genero = input("Intruduza su genero(hombre o mujer): ")
if Genero == "hombre":
    if nombre.lower()<"m":
        grupo = "A"
    else:
        grupo = "B"
else: 
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Nombre: "+ nombre +", "+ "Genero: "+Genero+" ==> "+grupo) 
