n = int(input("Intoducir numero entero: "))
def eval_primo(n):
    contador=0
    resultado=True
    for i in range(1,n+1):
        if(n%i==0):
            contador+=1
        if(contador>2):
            resultado=False
            break
    return resultado
if (eval_primo(n)==True):
    print("El numero es primo")
else:
    print("El numero no es primo")
    