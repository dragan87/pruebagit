"""Escriu un programa a Python que calculi el Màxim Comú Divisor (MCD) de dos números ingressats per l'usuari.

Instruccions:

    Demaneu a l'usuari que introdueixi dos nombres enters positius.
    Implementa un codi que calcula el MCD dels dos números utilitzant l'algorisme d'Euclides.
    Mostra el resultat del càlcul del MCD.
"""

a = int(input("introduce un entero: "))
b = int(input("introduce un entero: "))
mas_grande2= 0
mas_grande = 0
for i in range (2, a):
    if a%i== 0 and b%i == 0:
        mas_grande = i
print(mas_grande)

        
