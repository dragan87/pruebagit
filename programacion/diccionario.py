"""Escriviu un programa a Python que permeti portar un registre de dispositius de xarxa en un diccionari. Cada dispositiu té un nom i una adreça IP. 
El programa ha de permetre afegir dispositius, eliminar dispositius i llistar tots els dispositius registrats.

Instruccions:

    Crea un diccionari buit per emmagatzemar els dispositius, on les claus són els noms dels dispositius i els valors són les adreces IP.
    Permet a l'usuari afegir un dispositiu al diccionari.
    Permet a l'usuari eliminar un dispositiu del diccionari.
    Mostra tots els dispositius registrats al diccionari.

El programa ha de demanar contínuament a l'usuari quina acció ha de fer, fins que aquest esculli sortir.
"""
AFEGIR = 1
ELIMINAR = 2
MOSTRAR= 3
SALIR = 4
diccionario = {}
fin_programa = False
i = 0
borrar = False
while fin_programa == False:
    opcion = int(input("Escoge entre las siguientes opciones: 1- Afegir servidor, 2- Eliminar servidor, 3- Mostrar servidores: "))
    if opcion == AFEGIR:
        indice = input("Introduce el indice: ")
        dispositivo = input("nombre del dispositivo: ")
        diccionario[indice] = dispositivo
    else:
        if opcion == ELIMINAR:
            eliminar= input("introduce el dispositivo a eliminar : ")   
            for maquinas in diccionario.keys():
                if maquinas == eliminar:
                    borrar = True
            if borrar == True:
                del(diccionario[eliminar])
                    
        else:
            if opcion == MOSTRAR:
                for maquinas in diccionario.keys():
                    print(maquinas)
                    print(diccionario[maquinas])
            else:
                if opcion ==SALIR:
                    fin_programa = True
