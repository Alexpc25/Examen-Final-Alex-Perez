# Examen-Final-Alex-Perez

#Ejercicio nº1: 

```
import random
import collections

def numeros():
    x = int(input("Introduzca un número entre 0 y 9999: "))
    for i in range (2):
        while  type(x)!=int or x<0 or x>9999:
            try:
                x = int(x)
            except:
                pass
            if type(x)==int and x>=0 and x<=9999:
                break
            x= input("Error, introduzca un número adecuado: ")
    return x

n = list(str(numeros()))
m = list(str(numeros()))

print(n)
print(m)

if(collections.Counter(n)==collections.Counter(m)):
    print("Los número tienen los mismo digitos")
        
else:
    print("Los números no tienen los mismos digitos")
```

#Ejercicio nº2: 
  He hecho que el numero de dados lanzados sea como mucho 15 y que se sume el resultado de cada dado. Luego, la puntuación de los dados se divide entre 2 y se compara con la suma de los números elegidos por el jugador para determinar quién ha ganado. 
  
```
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
```

#Ejercicio nº3:
```
import random
def tirar_dados(x,y):
    while x != y:
        x = random.randint(1,6)
        y = random.randint(1,6)
    return x

print("Este juego es para 2 jugadores")

jug1 = tirar_dados(0,1)
jug2 = tirar_dados(0,1)

if jug1 > jug2: 
    print("La puntuacion del jugdor 1 es", jug1, "y la del jugador 2 es", jug2, "¡El jugador 1 ha ganado!")
if jug1 < jug2: 
    print("La puntuacion del jugdor 1 es", jug1, "y la del jugador 2 es", jug2, "¡El jugador 2 ha ganado!")
else:
    print("La puntuacion del jugdor 1 es", jug1, "y la del jugador 2 es", jug2,"Ha habido un empate")
```
