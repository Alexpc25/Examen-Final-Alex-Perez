import random

def numeros():
    x = int(input("Introduzca un número mayor que 0: "))
    for i in range (3):
        while  type(x)!=int or x<0:
            try:
                x = int(x)
            except:
                pass
            if type(x)==int and x>=0:
                break
            x= input("Error, introduzca un número adecuado: ")
    return x

def dados(): 
    b = 0
    y = random.randint(0,15)
    for i in range(y):
        a = random.randint(1,6)
        b += a
    return b

n1 = numeros()
n2 = numeros()
n3 = numeros()

punt_jug = n1+n2+n3

punt_dados = dados()

if punt_jug*2 > punt_dados:
    print("¡Ha ganado el juego!")
if punt_jug*2 < punt_dados:
    print("Ha perdido")
if punt_jug*2 == punt_dados:
    print("Empate")


