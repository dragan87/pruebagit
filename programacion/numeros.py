def numeros():
    #PRE: recivimos dos numeros enteros 
    #CONST
    INTRODUCIR_NUMEROS = "Introduce un numero entero : "
    INTRODUCE_OPERACION = "El 1 para una suma y el 2 para una resta: "
    SUMA = 1
    RESTA = 2

    #VARIABLES
    a = None
    b = None
    operando = None
    #END VAR

    a = int(input(INTRODUCIR_NUMEROS))
    operando = int(input(INTRODUCE_OPERACION))
    b = int(input(INTRODUCIR_NUMEROS))
    if operando == SUMA:
        suma = a + b
        print(suma)
    else:
        resta = a - b
        print(resta)
numeros()

