"""Escriu un programa a Python que verifiqui si un número ingressat per l'usuari és primer o no. Un nombre primer és aquell que només és divisible per 1 
i per si mateix.

Instruccions:

    Demaneu a l'usuari que introduïu un nombre enter.
    Verifica si el nombre és més gran que 1. Si és menor o igual a 1, indica-li a l'usuari que introdueixi un número vàlid.
    Implementa un bucle per verificar si el número és primer. Pots fer-ho comprovant si és divisible per algun número entre 2 i l'arrel quadrada del número.
    Mostra un missatge que indiqui si el número és primer o no.
    Si vols, pots proporcionar una explicació addicional sobre què significa ser un nombre primer.
"""

def division():
    a = int(input("dale un valor entero a la variable:" ))
    primo =("")
    if a <= 1:
        a = int(input("introdueixi un número vàlid"))
    for i in range (2,a):
        if((a%i) == 0):
            primo = "no es primo"
            break
        else:
             primo = "esPrimo"
    print(primo)
division()
        