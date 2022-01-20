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
    


