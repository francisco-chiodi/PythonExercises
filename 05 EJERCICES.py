"""
Desarrollar un programa para simular el juego de dados que se describe a continuación:

Inicio del Juego
Participan 2 jugadores. Para comenzar, se debe ingresar el puntaje récord del juego. Los jugadores deberán
acumular puntos en dos rondas para ganar y (eventualmente) superar el récord.

Primera Ronda
Se lanzan 2 dados. El puntaje en juego es el total de los dados. Si la suma de ambos dados es impar, el
 jugador 1 se queda con el puntaje y el jugador 2 con 0 puntos. Si la suma es par, el puntaje se asigna
 al jugador 2 mientras que el jugador 1 queda con 0.

Segunda Ronda
Se lanzan nuevamente los 2 dados. Si la suma de ambos es impar, al jugador 1 se le agregan tantos puntos como
 indique el dado de mayor valor, mientras que al jugador 2 se le quitan tantos puntos como indique el dado de
 menor valor. Si la suma es par, sucede lo contrario: el jugador 2 suma a su puntaje el dado de mayor valor y
 el jugador 1 resta el de menor valor.

Determinación del Ganador
El jugador que haya obtenido mayor puntaje será el ganador (considerar que pueden empatar). Informar además si
 el récord fue superado por alguno de ellos (o ambos)

"""

import random
record = int(input("record is: ", ))
player_1 = 0
player_2 = 0
dice_1 = random.randint(1,6)
dice_2 = random.randint(1,6)
dice_sum = dice_1 + dice_2
score = dice_sum
even = dice_sum % 2

if even != 0:
    player_1 = score
    player_2 = 0
    print("The winner is player one: ",player_1, "player two had: ", player_2)
elif even == 0:
    player_1 = 0
    player_2 = score
    print("The winner is player two: ",player_2, "player one had: ", player_1)

#second round Se lanzan nuevamente los 2 dados. Si la suma de ambos es impar,
# al jugador 1 se le agregan tantos puntos como indique el dado de mayor valor,
# mientras que al jugador 2 se le quitan tantos puntos como indique el dado de menor valor.
#Si la suma es par, sucede lo contrario: el jugador 2 suma a su puntaje el dado de mayor valor y
#el jugador 1 resta el de menor valor.

dice_3 = random.randint(1,6)
dice_4 = random.randint(1,6)
dices_max = max(dice_3, dice_4)
dices_min = min(dice_3, dice_4)
player_one = 0
player_two = 0

if even !=0:
    payer_one = player_1 + dices_max
    player_two = player_2 - dices_min
    print("the winner is player one: ",player_one,"player two had: ", player_two)

elif even == 0:
    player_one = player_1 - dices_min
    player_two = player_2 + dices_max
    print("the winner is player two: ", player_two,"player one had: ", player_one)

elif player_one > player_two and player_one > record:
    print("the winner is player one and the record was passedd: ", player_one , "previous record: ", record )
elif player_one > player_two:
    print("the winner is player one and the record was not passedd: ", player_one , "record is: ", record )

elif player_two > player_one and player_two > record:
    print("the winner is player two and the record was passedd: " , player_two , "previous record: ", record )
elif player_two > player_one:
    print("the winner is player two and the record was not passedd: ", player_two, "previous record: ", record)

#Determinación del Ganador
#El jugador que haya obtenido mayor puntaje será el ganador (considerar que pueden empatar).Informar además
#si el récord fue superado por alguno de ellos (o ambos)



