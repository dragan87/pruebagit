"""Escriviu un programa a Python que generi una llista de nombres primers en un rang específic ingressat per l'usuari.

Instruccions:

    Demana a l'usuari que introdueixi un rang (número inicial i número final) per cercar nombres primers.
    Genera una llista de nombres primers en aquest rang.
    Mostra la llista de nombres primers trobats.
"""
a = int(input("introduce un entero: "))
b = int(input("introduce un entero: "))
"""for i in range (a, b):
    for j in range (2, i):
        if i%j == 0 and j < i:
            break
        else: 
            print(i)
   """
lista = [None] * b
lista[0] = a
j = 1
k = a
i = 2
while k <= b:
    while i <= k:
        if k%i == 0 and i < k:
            break
        if k%i == 0 and i == k:
            lista[j] = k
        i+= 1
    i = 2
    k+= 1
    j+=1
print(lista)
        

    



        
