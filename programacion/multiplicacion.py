def calculadora():
    #PRE: recivimos dos numeros enteros 
    #CONST
    INTRODUCIR_NUMEROS = "Introduce un numero entero : "
    INTRODUCE_OPERACION = "El 1 para una suma el 2 para una resta 3 para multiplicacion y 4 para division: "
    SUMA = 1
    RESTA = 2
    MULTIPLICACION = 3
    DIVISION = 4
    #VARIABLES
    a = None
    b = None
    operando = None
    #END VAR

    a = int(input(INTRODUCIR_NUMEROS))
    b = int(input(INTRODUCIR_NUMEROS))
    operando = int(input(INTRODUCE_OPERACION))
    if operando == SUMA:
        suma = a + b
        print(suma)
    elif operando == MULTIPLICACION:
        multiplicacion = a * b
        print(multiplicacion)
    elif operando == DIVISION:
        if a == 0 or b == 0:            
            a = int(input(INTRODUCIR_NUMEROS))
            b = int(input(INTRODUCIR_NUMEROS))
        division = a // b 
        print(division)   
    else:
        resta = a - b
        print(resta)
calculadora()
