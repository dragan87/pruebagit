cartas = ['As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', '10s', 'Js', 'Qs', 'Ks', 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h', 'Jh', 'Qh', 'Kh', 'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', '10c', 'Jc', 'Qc', 'Kc', 'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', '10d', 'Jd', 'Qd', 'Kd']


jugadores = [[],[],[],[]]
for i in range(0,13):
    for j in range (0,4):
        jugadores[j].append(cartas.pop())	
"""index = 1
for jugador in jugadores:
    print("jugador", index, ": ",", ".join(jugador))
    print("cartas repartidas al jugador:",len(jugador))
    print()
    index +=1
"""
mesa = []
for jugador in jugadores:
    mesa.append(jugador.pop(0))
mismopalo = False
palo = []
letra = len(mesa[0]) - 1
print(letra)
print("hola")
for i in range len(mesa):
    if letra == len(mesa[i])-1:
        palo.append(mesa[i])
    ##iduhgsihfdiuhfiusdhfius

