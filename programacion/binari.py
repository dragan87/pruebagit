"""Escriu un programa a Python que converteixi un número binari ingressat per l'usuari al seu equivalent decimal.

Instruccions:

    Demana a l'usuari que introdueixi un número binari (una cadena de 0s i 1s).
    Converteix el número binari al seu equivalent decimal.
    Mostra el resultat de la conversió.
    """
frase = []
aux = []
final_texto = False
size_variable = 1
multiplicacion = 0
frase = list(input("escribe una cade de ceros y unos ")
while not final_texto:
    aux = [None] * size_variable 
    for j in range(0,size_variable):
        aux[j] = frase[j]
    if aux == frase:
        final_texto = True  
    size_variable+=1
for i in range (size_variable):
        multiplicacion = int((aux[i]**j)) + multiplicacion
        j+=1

print(multiplicacion)

"""binario = list(input("escribe una cadena de numeros binarios: "))
i = 0
size = 1
final= False
resultado = 0
while not final:
    aux = [None] * size
    for j in range (0, size):
        aux[j] = binario[j]
    if aux == binario:
        final = True
    
    resultado = (resultado * 2) + int(binario[i])
    i = i +1
    size+=1
print(resultado)
"""