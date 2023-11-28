
"""Escriu un programa a Python que generi els primers N números de la sèrie de Fibonacci, on N és un número ingressat per l'usuari.
Instruccions:

    Demaneu a l'usuari que introduïu un nombre enter positiu N.
    Genera els primers N números de la sèrie de Fibonacci.
    Mostra la sèrie de Fibonacci generad
    """
a = int(input("introducce un numero: "))
terme1= 0
terme2= 1
terme3= 0
"""while(terme3 <= a): 
    terme1 = terme2
    terme2 = terme3
    terme3 = terme1 + terme2
    print(terme3)
"""
for i in range (0, a):
    terme1 = terme2
    terme2 = terme3
    terme3 = terme1 + terme2
    print(terme3)
