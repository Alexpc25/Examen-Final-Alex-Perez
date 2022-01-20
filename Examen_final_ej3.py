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
