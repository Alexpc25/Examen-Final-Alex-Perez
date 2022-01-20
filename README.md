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

#Ejercicio nº3:
