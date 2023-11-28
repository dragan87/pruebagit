"""Escriviu un programa a Python que permeti gestionar una llista d'usuaris en un sistema. 
El programa ha de proporcionar les funcionalitats següents: afegir un usuari, eliminar un usuari i llistar tots els usuaris.

Instruccions:

    Creeu una llista buida per emmagatzemar els noms d'usuari.
    Permet a lusuari afegir un nom a la llista.
    Permet a lusuari eliminar un nom de la llista.
    Mostra tots els noms d'usuari emmagatzemats.

El programa a de demanar constantment que vol fer l'usuari, fins que aquest esculli l'opció de sortir.
"""
AFEGIR = 1
ELIMINAR = 2
LLISTAR = 3
SALIR = 4

lista = []
nombre = ""
fin_del_programa = False

while fin_del_programa == False:
    opcion = int(input("Que quieres hacer 1- Afegir, 2- Eliminar, 3- Llistar, 4- Salir: "))

    if opcion == AFEGIR:
        nombre = input("Introduce el nombre del usuario: ")
        lista.append(nombre)    
    else:
        if opcion == ELIMINAR:
            nombre = input("Introduce el nombre del usuario a eliminar: ")
            if lista.count(nombre) > 0:
                lista.remove(nombre)
        else:
            if opcion == LLISTAR:
                for i in range(0, len(lista)):
                    print(lista[i])
            else: 
                fin_del_programa = True
            
        