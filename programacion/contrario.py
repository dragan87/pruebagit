"""Donades dues cadenes: s1 i s2. Si són oposats, retorna true; en cas contrari, retorna false. 
Nota: el resultat hauria de ser un valor booleà, en lloc d'una cadena.

Oposat vol dir: totes les lletres de les dues cadenes són iguals, però si és majúscula o minúscula és oposat. 

Podeu suposar que la cadena només conté lletres o que és una cadena buida. També tingueu en compte el cas extrem: si ambdues cadenes estan buides, haureu de tornar false / False.

Exemples (entrada -> sortida)
    "ab","AB"            -> true
    "aB","Ab"            -> true
    "aBcd","AbCD"  -> true
    "AB","Ab"           -> false
    "",""                     -> false
    """

#el usuario tiene que pasarnos dos cadenas de texto
s1 = input("escribeme la primera cadena: ")
s2 = input("escribeme la segunda cadena: ")
#mirar si las cadenas son iguales 
print(s1[0])
if len(s1[0]) == len(s2[0]):
    print("hola")
else:
    print("keko")
  